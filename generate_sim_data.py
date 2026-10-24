import json
import math
import os

# Create the public directory if it doesn't exist yet
os.makedirs('/home/omy-archy/ecosport-obd-poc/frontend/public', exist_ok=True)

data = []
# Simulate 180 seconds (3 minutes) of driving data at 10Hz (1800 samples)
# We will use 10Hz to make the dashboard animation smooth
total_seconds = 180
hz = 10
total_samples = total_seconds * hz

for i in range(total_samples):
    t = i / hz
    
    # Base baseline from recorded idle
    rpm = 780
    speed = 0
    load = 0.0
    throttle = 0.0
    
    # Simple driving profile
    if t < 10:
        # Idle (using baseline logic, adding slight noise)
        rpm = 780 + math.sin(t * 2) * 15
        speed = 0
        load = 15.0 + math.cos(t) * 2
    elif t < 40:
        # Accelerate to 80 km/h
        progress = (t - 10) / 30.0
        speed = progress * 80
        # Simulate gear shifts (1st, 2nd, 3rd, 4th, 5th)
        gear = min(5, max(1, int(1 + speed // 16)))
        # RPM rises then drops on shift
        rpm = 1200 + ((speed % 16) / 16.0) * 1800
        load = 60.0 + math.sin(t * 5) * 5
    elif t < 100:
        # Cruising at 80 km/h with some traffic variance
        speed = 80 + math.sin(t / 4.0) * 5
        rpm = 2100 + math.sin(t / 4.0) * 100
        load = 35.0 + math.cos(t / 2.0) * 10
    elif t < 120:
        # Heavy braking to 0
        progress = (t - 100) / 20.0
        speed = max(0, 80 * (1.0 - progress))
        gear = max(1, int(1 + speed // 16))
        rpm = 1000 + speed * 15
        load = 10.0
    elif t < 150:
        # Idle at red light
        rpm = 780 + math.sin(t * 2) * 15
        speed = 0
        load = 15.0 + math.cos(t) * 2
    else:
        # Light acceleration again
        progress = (t - 150) / 30.0
        speed = progress * 40
        rpm = 1200 + ((speed % 16) / 16.0) * 1800
        load = 45.0
        
    # Add high-frequency jitter for realism
    rpm += math.sin(t * 50) * 20
    speed += math.sin(t * 20) * 0.5
    
    # Engine temp slowly rises from baseline
    temp = 33 + (t / total_seconds) * 55 # Rises from 33C to 88C
    
    # Throttle roughly tracks load
    throttle = min(100.0, max(0.0, load * 1.2 + math.sin(t*10)*5))

    data.append({
        "time_s": round(t, 1),
        "RPM": max(0, int(rpm)),
        "Speed_kmh": max(0, int(speed)),
        "Engine_Load": max(0.0, round(load, 1)),
        "Coolant_Temp": int(temp),
        "Throttle_Pos": max(0.0, round(throttle, 1))
    })

with open('/home/omy-archy/ecosport-obd-poc/frontend/public/simulated_drive.json', 'w') as f:
    json.dump(data, f)

print(f"Generated {len(data)} simulated samples.")
