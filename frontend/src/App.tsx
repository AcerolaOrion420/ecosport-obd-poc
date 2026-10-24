import { createSignal, onMount, onCleanup, createMemo } from 'solid-js';

type Datapoint = {
  time_s: number;
  RPM: number;
  Speed_kmh: number;
  Engine_Load: number;
  Coolant_Temp: number;
  Throttle_Pos: number;
};

// SVG Arc gauge
function ArcGauge(props: {
  value: number; max: number; label: string; unit: string; color: string;
}) {
  const cx = 100, cy = 95, r = 70;
  const startDeg = -120, endDeg = 120;

  const toRad = (d: number) => ((d - 90) * Math.PI) / 180;

  const bgPath = () => {
    const s = toRad(startDeg), e = toRad(endDeg);
    return `M ${cx + r * Math.cos(s)} ${cy + r * Math.sin(s)} A ${r} ${r} 0 1 1 ${cx + r * Math.cos(e)} ${cy + r * Math.sin(e)}`;
  };

  const fgPath = () => {
    const frac = Math.min(props.value, props.max) / props.max;
    if (frac < 0.01) return '';
    const end = startDeg + frac * (endDeg - startDeg);
    const s = toRad(startDeg), e = toRad(end);
    const large = end - startDeg > 180 ? 1 : 0;
    return `M ${cx + r * Math.cos(s)} ${cy + r * Math.sin(s)} A ${r} ${r} 0 ${large} 1 ${cx + r * Math.cos(e)} ${cy + r * Math.sin(e)}`;
  };

  return (
    <div class="bg-slate-800/60 border border-slate-700 rounded-2xl p-6 flex flex-col items-center w-72">
      <svg viewBox="0 0 200 130" width="200" height="130">
        <path d={bgPath()} stroke="#334155" stroke-width="14" fill="none" stroke-linecap="round" />
        <path d={fgPath()} stroke={props.color} stroke-width="14" fill="none" stroke-linecap="round"
          style="transition: d 0.12s ease-out;" />
        <text x="100" y="100" text-anchor="middle" font-size="42" font-weight="800"
          fill="#f8fafc" font-family="ui-monospace, monospace">
          {Math.floor(props.value)}
        </text>
        <text x="100" y="120" text-anchor="middle" font-size="11" fill="#94a3b8"
          font-weight="600" letter-spacing="2">{props.unit}</text>
      </svg>
      <span class="text-xs text-slate-400 font-semibold tracking-widest mt-1">{props.label}</span>
    </div>
  );
}

// Bar stat card
function StatCard(props: { label: string; value: number; max: number; unit: string; color: string }) {
  const pct = () => Math.min(100, (props.value / props.max) * 100);
  return (
    <div class="bg-slate-800/60 border border-slate-700 rounded-xl p-4">
      <div class="text-slate-400 text-xs font-semibold tracking-wider mb-2">{props.label}</div>
      <div class="flex items-baseline gap-1">
        <span class="text-2xl font-bold font-mono text-white">{props.value.toFixed(1)}</span>
        <span class="text-slate-500 text-sm">{props.unit}</span>
      </div>
      <div class="mt-2 h-1.5 rounded-full bg-slate-900 overflow-hidden">
        <div class={`h-full rounded-full transition-all duration-100`}
          style={`width: ${pct()}%; background: ${props.color};`} />
      </div>
    </div>
  );
}

export default function App() {
  const [data, setData] = createSignal<Datapoint[]>([]);
  const [idx, setIdx] = createSignal(0);
  const [playing, setPlaying] = createSignal(false);
  let timer: number;

  onMount(async () => {
    const res = await fetch('/simulated_drive.json');
    setData(await res.json());
  });

  onCleanup(() => clearInterval(timer));

  const toggle = () => {
    if (playing()) {
      clearInterval(timer);
      setPlaying(false);
    } else {
      if (idx() >= data().length - 1) setIdx(0);
      setPlaying(true);
      timer = window.setInterval(() => {
        setIdx(i => {
          if (i >= data().length - 1) { clearInterval(timer); setPlaying(false); return i; }
          return i + 1;
        });
      }, 100);
    }
  };

  const reset = () => { clearInterval(timer); setPlaying(false); setIdx(0); };

  const d = createMemo(() => data()[idx()] || null);

  const rpmColor = createMemo(() => {
    const rpm = d()?.RPM || 0;
    if (rpm > 3500) return '#ef4444';
    if (rpm > 2200) return '#f59e0b';
    return '#22c55e';
  });

  const timeStr = createMemo(() => {
    const t = d()?.time_s || 0;
    const total = data().length ? data()[data().length - 1].time_s : 0;
    const fmt = (s: number) => `${Math.floor(s / 60)}:${String(Math.floor(s % 60)).padStart(2, '0')}`;
    return `${fmt(t)} / ${fmt(total)}`;
  });

  return (
    <div class="min-h-screen bg-slate-950 text-slate-100 font-sans p-6 flex flex-col items-center">
      <div class="w-full max-w-3xl flex flex-col gap-5">

        {/* Header */}
        <div class="flex items-center justify-between">
          <div>
            <h1 class="text-xl font-bold tracking-tight text-white">EcoSport OBD-II Dashboard</h1>
            <p class="text-slate-500 text-xs mt-0.5 tracking-wide">VIN MAJAXXMRKAFE35942 · Simulated Drive Replay</p>
          </div>
          <div class="flex gap-2">
            <button onClick={toggle}
              class="px-5 py-2 text-sm font-semibold rounded-lg bg-cyan-600 text-white hover:bg-cyan-500 transition">
              {playing() ? '⏸ Pause' : '▶ Play'}
            </button>
            <button onClick={reset}
              class="px-4 py-2 text-sm font-semibold rounded-lg bg-slate-800 text-slate-300 border border-slate-700 hover:bg-slate-700 transition">
              Reset
            </button>
          </div>
        </div>

        {data().length === 0 ? (
          <div class="text-center py-20 text-cyan-500 animate-pulse font-semibold">Loading drive data...</div>
        ) : (
          <>
            {/* Gauges */}
            <div class="flex gap-5 justify-center flex-wrap">
              <ArcGauge value={d()?.Speed_kmh || 0} max={120} label="SPEED" unit="KM/H" color="#06b6d4" />
              <ArcGauge value={d()?.RPM || 0} max={6000} label="TACHOMETER" unit="RPM" color={rpmColor()} />
            </div>

            {/* Stats */}
            <div class="grid grid-cols-3 gap-4">
              <StatCard label="ENGINE LOAD" value={d()?.Engine_Load || 0} max={100} unit="%" color="#8b5cf6" />
              <StatCard label="THROTTLE" value={d()?.Throttle_Pos || 0} max={100} unit="%" color="#f59e0b" />
              <StatCard label="COOLANT TEMP" value={d()?.Coolant_Temp || 0} max={120} unit="°C" color="#ef4444" />
            </div>

            {/* Timeline */}
            <div class="bg-slate-800/60 border border-slate-700 rounded-xl p-4">
              <div class="flex justify-between items-center mb-2">
                <span class="text-xs text-slate-400 font-semibold tracking-wider">TIMELINE</span>
                <span class="text-sm font-mono font-bold">{timeStr()}</span>
              </div>
              <input type="range" min="0" max={data().length - 1} value={idx()}
                onInput={(e) => setIdx(parseInt(e.currentTarget.value))}
                class="w-full h-1.5 bg-slate-900 rounded-full appearance-none cursor-pointer accent-cyan-500" />
            </div>
          </>
        )}
      </div>
    </div>
  );
}
