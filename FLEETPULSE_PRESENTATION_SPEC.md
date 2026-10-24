
Create a professional, visually rich presentation titled **"FleetPulse: A Privacy-First, BYOD Fleet Management & Rental Vehicle Monitoring Platform"** for an MCA (Master of Computer Applications) academic project.

**Design direction**: Modern and corporate. Use a clean dark navy/slate background with electric blue and teal accents. Each slide should feel like an enterprise product pitch deck — confident, clear, data-driven. Include space for diagrams, icons, and data visualizations where indicated. Font pairing: a bold geometric sans-serif for headings, clean readable body font.

**Audience**: University faculty panel, classmates, and a simulated investor/client audience.
**Length**: 20–22 slides.

---

### SLIDE 1 — Cover

**Title**: FleetPulse
**Subtitle**: Real-Time Fleet Intelligence for the Modern Rental Operator
**Tagline**: *Know everything. Own everything. Control everything.*
Name: Omkar R Reddy, USN: 1BY25MC069, ProjectGuide: Prof. Nirupama B K

Background visual suggestion: Top-down view of cars on a highway with a subtle data overlay (hexagonal grid, pulsing lines)

---

### SLIDE 2 — The Problem with Running a Fleet Today

Fleet and rental operators are flying blind:

- **No real-time engine visibility** — owners learn about breakdowns from distressed renters, not dashboards
- **Driver abuse goes unpunished** — renters over-rev, idle for hours, drive aggressively — owners can't prove it
- **Calendar servicing wastes money** — vehicles are serviced on schedule, not on condition; some are over-serviced, some fail between services
- **Expensive proprietary hardware** — enterprise fleet solutions (Samsara, MiX Telematics) require ₹15,000–₹50,000 per vehicle in custom hardware
- **No blackbox for accidents** — when accidents happen, there's no record of vehicle speed, engine state, or driver behaviour in the moments before impact
- **Data owned by vendors** — fleet data lives on someone else's servers, under someone else's terms

Visual: Split image — stressed fleet manager with phone on one side, data dashboard on the other

---

### SLIDE 3 — The Market Opportunity

- India's fleet management market: **₹17,000 crore+ by 2027** (15.3% CAGR)
- **12 million+ commercial vehicles** in India, all OBD-II equipped since BS-IV (2017)
- Self-drive rental market growing at **25% CAGR** — Zoomcar, Revv, and hundreds of local operators
- Most operators still use **WhatsApp groups and Excel sheets** for fleet management
- Affordable, diagnostics-rich fleet monitoring for Indian operators: **virtually nonexistent**

Visual: India map with fleet density overlay, market size infographic

---

### SLIDE 4 — Introducing FleetPulse

**What it is**: A locally-hosted fleet management platform that turns every vehicle's OBD-II port into a continuous stream of real-time intelligence — without any proprietary hardware.

**What it does**:
- Streams live engine and GPS data from every deployed vehicle
- Predicts mechanical failures weeks before they happen
- Monitors and scores driver behaviour on every trip
- Acts as a digital blackbox for accident investigation
- Analyses fuel consumption per vehicle and per driver
- Gives owners complete data ownership — hosted on their own infrastructure

**What it costs to deploy**: A ₹500 ELM327 Bluetooth adapter per vehicle. The driver's own smartphone does the rest.

Visual: Clean product screenshot mockup of the dashboard

---

### SLIDE 5 — How It Works: The BYOD Architecture

**BYOD = Bring Your Own Device**

FleetPulse uses the driver's existing smartphone as the intelligent edge device:

1. **ELM327 Bluetooth OBD-II adapter** plugs into the vehicle's diagnostic port (₹500, fits all OBD-II vehicles)
2. **Driver's phone** connects to the adapter via Bluetooth and runs the FleetPulse mobile relay app
3. The app simultaneously captures **OBD-II engine data + GPS location** and streams it over the phone's mobile data connection
4. Data flows to the **FleetPulse server** — hosted locally at the fleet owner's office or on a private cloud instance
5. The fleet manager opens the **web dashboard** on any browser to see the entire fleet in real time

Diagram: Vehicle → OBD adapter → Phone (BT + GPS) → Internet → Private Server → Dashboard

**Why this is revolutionary**: No SIM card in the vehicle, no custom hardware, no vendor lock-in. Just a ₹500 plug and the phone every driver already carries.

---

### SLIDE 6 — Real-Time Telemetry: What We Actually Capture

From our live proof-of-concept scan of a Ford EcoSport, we confirmed **72 supported PIDs (Parameter IDs)** across 9 categories:

| Category | Key Data Points |
|---|---|
| Engine Core | RPM, Engine Load, MAF Rate, MAP Pressure |
| Temperatures | Coolant, Oil, Intake Air, Ambient, Exhaust Gas |
| Fuel System | Rail Pressure, Injection Timing, EGR Position |
| Turbo & Boost | Boost Pressure, VGT Control, Turbo RPM, Wastegate |
| Throttle & Pedal | Throttle Position, Accelerator Pedal Position |
| Emissions | DPF Pressure, DPF Temperature, NOx Status |
| Electrical | Battery/Module Voltage, Monitor Status |
| History | Distance Since Service Clear, Warm-up Count, MIL Time |
| Vehicle Identity | VIN, Calibration ID, ECU Name, OBD Standard |

Plus: **GPS coordinates, speed, heading, altitude** from the phone

This is not theoretical — this data was captured live from a real vehicle for this project.

---

### SLIDE 7 — Feature: Predictive Maintenance

**The core insight**: Engines don't fail suddenly. They fail slowly — and the OBD-II port shows the decline in real time.

**How FleetPulse predicts failures**:

- **Cooling system failure** (most common breakdown): Coolant temp trends upward across trips from a normal 87°C baseline → FleetPulse alerts owner weeks before it hits a dangerous 110°C+
- **Battery/alternator failure**: Charging voltage declining from 14.2V → 13.8V → 13.2V across weeks of recorded trips predicts a stranded vehicle
- **DPF clogging** (diesel): Rising differential pressure across the particulate filter predicts a complete blockage — an ₹80,000+ replacement if missed
- **Turbocharger degradation**: Boost pressure not reaching expected levels at given throttle positions indicates turbo wear — catch it early vs. replace it
- **Pending DTCs (Mode 07)**: The ECU stores "near-fault" codes before the check engine light turns on. FleetPulse reads these first-warning codes and alerts owners immediately

**The result**: Condition-based maintenance instead of calendar-based. Service when the vehicle needs it, not when the calendar says to.

Visual: Temperature trend graph showing gradual rise with alert threshold marked

---

### SLIDE 8 — Feature: Fleet Health Dashboard

Every vehicle in the fleet gets a **Health Score (0–100)** calculated from:
- Active and pending fault codes (DTCs)
- Coolant and oil temperature trends
- Battery voltage trend
- DPF differential pressure
- Time since last service clear
- Abnormal sensor readings

**Dashboard shows at a glance**:
- 🟢 Green: Healthy, ready to deploy
- 🟡 Amber: Minor issues, monitor closely
- 🔴 Red: Do not deploy — needs attention

Fleet managers can prevent a mechanically compromised vehicle from being handed to a paying renter — protecting both the client's safety and the operator's liability.

Visual: Grid of vehicle cards with health score indicators

---

### SLIDE 9 — Feature: Digital Blackbox & Accident Investigation

**The problem with accidents today**: No objective record exists of what the vehicle was doing before impact. Blame is assigned based on witness accounts and damage patterns — both unreliable.

**FleetPulse acts as a continuous blackbox**:
Every second of every trip is recorded:
- GPS position, speed, heading
- Engine RPM and load
- Throttle and brake inputs (via pedal position PIDs)
- Vehicle speed (independent of GPS for cross-validation)
- Any fault codes that appeared

**Post-accident, the operator can produce**:
- Exact vehicle speed and location in the 60 seconds before impact
- Whether the driver was accelerating, braking, or coasting
- Whether any mechanical fault (brake system DTC, engine fault) was present
- A GPS track of the entire trip

**Who benefits**:
- **Insurance companies**: Objective data dramatically speeds up claim resolution and prevents fraud
- **Law enforcement**: Precise reconstruction of accident timeline and vehicle behaviour
- **Fleet operators**: Exonerate themselves when the vehicle was in good condition and the accident was driver error
- **Drivers**: Exonerate themselves when a sudden mechanical failure caused the accident

Visual: Split — accident scene photo on left, data replay timeline on right

---

### SLIDE 10 — Feature: Driver Behaviour Monitoring

**The problem**: Renters know they're anonymous. Without monitoring, there's no consequence for abuse.

**FleetPulse tracks and scores**:

| Behaviour | How Detected | Threshold |
|---|---|---|
| Aggressive acceleration | Engine load spike >80% + rapid RPM rise | Configurable |
| Harsh braking | Speed drop >20 km/h in <3 seconds | Configurable |
| Excessive idling | RPM >0 + Speed = 0 for >5 minutes | Configurable |
| Over-revving | RPM sustained above 4500 (diesel) | Per vehicle type |
| Speeding | GPS speed vs. road speed limit database | Per zone |

**Each driver gets a Trip Score (0–100)**
- Scores accumulate over the rental period
- Operators can set automatic alerts (score below 60 = notify manager)
- Repeat offenders can be flagged or blocked from future bookings
- Incentive programs: good scores earn discounts

**Data is timestamped and GPS-tagged** — every infraction has a when and where, making it impossible for drivers to dispute.

---

### SLIDE 11 — Feature: Fuel Consumption Analysis

**FleetPulse calculates real fuel economy without a fuel card system**:

- **Mass Air Flow (MAF) + Air-Fuel Ratio** → real-time litres/hour consumption
- **MAF ÷ Speed** → real-time litres/100km
- Integrated over a full trip → **total fuel consumed per trip**

**What this reveals**:

- **Per-vehicle fuel efficiency trends**: A vehicle consistently burning 15% more than fleet average likely has injector wear, low tyre pressure, or a partially clogged fuel system — catch it before it becomes a breakdown
- **Per-driver fuel impact**: Same vehicle, 14 km/L with Driver A, 10 km/L with Driver B → data-driven case for driver coaching
- **Idle fuel waste**: Quantify exactly how many litres are burned while vehicles sit idling — for a fleet of 20 vehicles idling 1 hour/day, that's potentially ₹3,000–₹5,000/month in recoverable waste
- **Trip-level cost accounting**: Know the actual fuel cost of every trip without requiring fuel card reconciliation

Visual: Bar chart comparing fuel efficiency across drivers and vehicles

---

### SLIDE 12 — Feature: GPS Tracking & Why It Matters

**GPS provides the geographic context that makes all other data meaningful**:

**Geofencing & Zone Control**
- Define allowed areas (city limits, state boundaries, delivery zones)
- Instant alert when a vehicle exits the authorised zone
- Automatic detection of unauthorised locations (unapproved workshops, competitor premises)

**Route Validation**
- Confirm vehicles are taking authorised routes
- Detect detours that add unexplained kilometres
- Validate delivery or passenger drop-off points

**Speed Limit Enforcement**
- GPS speed + road speed limit database = automatic speeding alerts with precise location
- "Vehicle exceeded 60 km/h in a 40 km/h school zone at 8:14 AM on 15th October" — specific and defensible

**Blackbox Reconstruction**
- GPS track provides the definitive travel path for accident investigation
- Cross-validates OBD-II speed readings (two independent speed sources increase evidence credibility)

**Stolen Vehicle Recovery**
- Last known GPS position immediately available if vehicle goes offline unexpectedly
- Phone continues reporting GPS after scanner is unplugged (theft window coverage)

**Anti-Odometer Fraud**
- GPS-calculated trip distance vs. OBD-II reported distance — discrepancies flag potential tampering

---

### SLIDE 13 — Privacy First: Local Hosting & Data Ownership

**Most fleet software is SaaS — your data lives on someone else's servers.**

FleetPulse is different:

- **Self-hosted**: The server runs on hardware the operator owns — a ₹15,000 mini PC at the office, or a private VPS they control
- **No third-party data sharing**: Vehicle location, engine data, and driver behaviour never leave the operator's infrastructure unless they choose to export it
- **GDPR/DPDP Act aligned**: India's Digital Personal Data Protection Act (2023) places obligations on data handlers. By keeping data local, operators have clear, simple compliance
- **Driver privacy**: Operators can configure what data is retained and for how long — building trust with drivers
- **No vendor lock-in**: Open architecture means operators can migrate, modify, or extend the platform without permission from a vendor

**Who cares about this**:
- Operators with sensitive commercial operations (banks, government contractors, defence suppliers)
- Operators in regions with poor or expensive internet — local hosting means the dashboard works on LAN even without internet
- Any operator who has experienced a SaaS vendor hiking prices or discontinuing a product

Visual: Comparison table — SaaS fleet software vs. FleetPulse (data location, cost, control, privacy)

---

### SLIDE 14 — Cost Advantage: The Numbers

**Competitor hardware cost per vehicle**:
- Samsara vehicle gateway: ~₹18,000–₹25,000
- MiX Telematics unit: ~₹20,000–₹30,000
- Fleetio + GPS hardware: ~₹15,000+
- Monthly SaaS fees: ₹1,500–₹5,000/vehicle/month

**FleetPulse cost per vehicle**:
- ELM327 Bluetooth OBD-II adapter: **₹500** (one-time)
- Driver's smartphone: ₹0 (BYOD — they already have it)
- Server: **₹0** (use existing office hardware) or ~₹800/month for a VPS (for entire fleet, not per vehicle)
- Software: **₹0** (open-source)

**For a 20-vehicle fleet**:
- Competitor: ₹4,00,000+ hardware + ₹30,000–₹1,00,000/month SaaS
- FleetPulse: ₹10,000 total hardware + minimal hosting cost

**The savings fund the maintenance the system recommends.**

Visual: Cost comparison bar chart, 1 year TCO comparison

---

### SLIDE 15 — Technical Architecture

**Three-layer architecture**:

**Edge Layer (Per Vehicle)**
- ELM327 Bluetooth OBD-II adapter
- Driver's Android/iOS phone running FleetPulse Relay App
- App captures: OBD-II PIDs via BT + GPS via phone hardware
- Streams data over HTTPS/WebSocket to server

**Backend Layer (Operator's Server)**
- Python/Node.js API server
- PostgreSQL for trip and event storage
- TimescaleDB for time-series sensor data (optimised for OBD-II streams)
- MQTT broker for real-time streaming
- Alert engine for DTC, temperature, behaviour triggers

**Frontend Layer (Fleet Manager's Browser)**
- SolidJS web dashboard — reactive, high-performance gauge rendering
- Real-time vehicle map (GPS positions)
- Trip replay with animated telemetry
- Driver behaviour reports and fleet health overview

Diagram: Three-layer architecture with technology labels

---

### SLIDE 16 — Proof of Concept: This Is Real

**We didn't just design this — we built and tested a working PoC**:

✅ Connected a Bluetooth ELM327 scanner to a **real Ford EcoSport**
✅ Discovered and read **72 supported PIDs** across 9 data categories
✅ Decoded the vehicle's **VIN** (MAJAXXMRKAFE35942), ECU name, and calibration data
✅ Confirmed **India OBD-II (IOBD-II) compliance** — Standard #32
✅ Verified **zero active fault codes** — clean vehicle
✅ Recorded a **132-second live data stream** at 3-second intervals
✅ Built an **interactive replay dashboard** with animated arc gauges
✅ Built a **CLI live-stream tool** proving real-time data capability

**Engineering challenges solved**:
- Non-standard RFCOMM channel discovery (channel 2, not standard 1)
- ELM327 sleep/wake behaviour workaround
- Multi-frame ISO 15765-4 response decoding for VIN and ECU name
- PID bitmask chain parsing (5 support registers, 72 total PIDs found)

Visual: Screenshot of CLI live stream + screenshot of dashboard

---

### SLIDE 17 — Driver Behaviour: The Business Case

**Why operators should care about driver behaviour beyond ethics**:

- **Tyre wear**: Aggressive cornering and harsh braking reduce tyre life by up to 40% — on a rental fleet, that's a direct cost to the operator
- **Brake wear**: Harsh braking wears brake pads 3–5x faster than smooth driving
- **Engine wear**: Sustained high-RPM driving and cold-engine abuse accelerate engine wear, reducing the vehicle's resale value and productive life
- **Fuel**: Aggressive driving burns 15–25% more fuel than smooth driving (calculable directly from MAF data)
- **Accident liability**: A driver with a consistently low behaviour score who causes an accident may expose the operator to liability if it can be shown the pattern was known and ignored

**FleetPulse makes the ROI on monitoring undeniable**: The reduction in tyre, brake, and fuel costs alone for a 20-vehicle fleet can fund the entire platform many times over.

---

### SLIDE 18 — Competitive Landscape

| Feature | FleetPulse | Samsara | Fleetio | MiX Telematics |
|---|---|---|---|---|
| Real OBD-II diagnostics | ✅ Full | ✅ Partial | ❌ | ✅ Partial |
| BYOD (no vehicle hardware needed) | ✅ | ❌ | ❌ | ❌ |
| Hardware cost per vehicle | ₹500 | ₹18,000+ | ₹15,000+ | ₹20,000+ |
| Indian IOBD-II support | ✅ | ❌ | ❌ | ❌ |
| Local/self-hosted | ✅ | ❌ | ❌ | ❌ |
| Driver behaviour scoring | ✅ | ✅ | ❌ | ✅ |
| Accident blackbox | ✅ | ✅ | ❌ | ✅ |
| Predictive maintenance | ✅ | ✅ | Basic | ✅ |
| Fuel analysis (from MAF) | ✅ Real-time | Estimated | ❌ | Estimated |
| Data ownership | Operator | Vendor | Vendor | Vendor |

**FleetPulse is the only solution combining full OBD-II diagnostics, BYOD, local hosting, and sub-₹1,000 hardware cost.**

---

### SLIDE 19 — Project Roadmap

**Phase 1 — Completed**: PoC — Bluetooth OBD-II connection, 72-PID discovery, live recording, replay dashboard
**Phase 2 — In Progress**: Multi-vehicle support, persistent trip storage, driver scoring, real-time WebSocket streaming
**Phase 3**: Mobile relay app (Android), GPS integration, geofencing, alert system
**Phase 4**: Predictive maintenance ML models, anomaly detection, DPF/coolant trend analysis
**Phase 5**: Insurance API integration, speed limit database, fleet cost analytics dashboard

Visual: Horizontal timeline/roadmap graphic

---

### SLIDE 20 — Impact Summary

**For Fleet Operators**:
- Complete visibility into every vehicle's health and location
- Reduce breakdown-related downtime and emergency repair costs
- Shift from reactive to predictive maintenance

**For Renters and Drivers**:
- Safer vehicles (pre-cleared before deployment)
- Faster insurance resolution with objective blackbox data
- Accountability that promotes better driving habits

**For the Industry**:
- Democratises fleet intelligence — accessible to operators with 5 vehicles, not just enterprises with 500
- Promotes data privacy and operator sovereignty
- Built specifically for Indian OBD-II vehicles (IOBD-II support)

---

### SLIDE 21 — Live Demo

"Let me show you the actual system working."

Demonstrate:
1. **CLI live stream**: Python script connects to the Bluetooth scanner, real-time RPM/Speed/Load/Temp printing in terminal — proving the data pipeline is real
2. **Web dashboard**: Replay of the recorded 132-second drive with animated arc gauges, timeline scrubber
3. **Raw data**: The JSON output file showing timestamped, decoded sensor readings from the actual Ford EcoSport

---

### SLIDE 22 — Thank You & Questions

**FleetPulse** proves that enterprise-grade fleet intelligence doesn't require enterprise-grade hardware budgets.

A ₹500 adapter. The driver's phone. Powerful, private, and yours.

*Questions?*
