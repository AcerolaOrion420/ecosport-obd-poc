#!/usr/bin/env python3
"""
EcoSport OBD-II Live CLI Dashboard
Connects to the BT ELM327 and prints a live-updating dashboard in the terminal.
"""

import socket
import subprocess
import time
import sys
import os

BT_ADDR = "01:23:45:67:89:BA"
BT_CHANNEL = 2

# Core driving PIDs
PIDS = [
    (0x0C, "RPM", "rpm", lambda d: int(((d[0]*256)+d[1])/4) if len(d)>=2 else 0),
    (0x0D, "SPD", "km/h", lambda d: d[0] if len(d)>=1 else 0),
    (0x04, "LOD", "%", lambda d: round(d[0]*100/255, 1) if len(d)>=1 else 0),
    (0x05, "TMP", "°C", lambda d: d[0]-40 if len(d)>=1 else 0),
]

def bt_connect(addr, channel):
    print("\033[96m[1/3] Waking up Bluetooth adapter...\033[0m")
    subprocess.Popen(['bluetoothctl', '--', 'connect', addr], 
                     stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).communicate(timeout=4)
    time.sleep(1)
    
    print(f"\033[96m[2/3] Opening RFCOMM socket on channel {channel}...\033[0m")
    sock = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
    sock.settimeout(8)
    sock.connect((addr, channel))
    return sock

def elm_send(sock, cmd, delay=0.15):
    sock.send(cmd if isinstance(cmd, bytes) else cmd.encode())
    time.sleep(delay)
    response = b""
    sock.settimeout(1.5)
    try:
        while True:
            chunk = sock.recv(4096)
            if not chunk: break
            response += chunk
            if b">" in chunk: break
    except socket.timeout:
        pass
    return response.decode('ascii', errors='replace').strip()

def extract_bytes(resp, pid):
    import re
    cleaned = resp.replace('>', '').replace('\r', '').replace('\n', ' ').strip()
    hex_str = ''.join(cleaned.split())
    expected = f"41{pid:02X}"
    idx = hex_str.upper().find(expected.upper())
    if idx == -1: return []
    data_hex = hex_str[idx + 4:]
    return [int(data_hex[i:i+2], 16) for i in range(0, len(data_hex)-1, 2) if all(c in '0123456789ABCDEFabcdef' for c in data_hex[i:i+2])]

def main():
    os.system('clear')
    print("=" * 60)
    print("\033[1;33m  FORD ECOSPORT - OBD-II LIVE CLI DASHBOARD\033[0m")
    print("=" * 60)
    
    try:
        sock = bt_connect(BT_ADDR, BT_CHANNEL)
        print("\033[96m[3/3] Initializing ELM327 Fast Mode...\033[0m")
        for cmd in [b"ATZ\r", b"ATE0\r", b"ATL0\r", b"ATH0\r", b"ATSP0\r", b"ATAT2\r"]:
            elm_send(sock, cmd, delay=0.5)
            
        print("\n\033[92mCONNECTED. STREAMING LIVE DATA...\033[0m (Press Ctrl+C to stop)\n")
        
        # Hide cursor
        sys.stdout.write("\033[?25l")
        sys.stdout.flush()
        
        while True:
            display = ["\033[1m"]
            for pid, name, unit, decoder in PIDS:
                resp = elm_send(sock, f"01{pid:02X}\r", delay=0.2)
                d = extract_bytes(resp, pid)
                val = decoder(d) if d else "--"
                
                # Color code based on value (e.g., Red RPM if > 4000)
                color = "\033[92m" # Green
                if name == "RPM" and isinstance(val, int):
                    if val > 4000: color = "\033[91m"
                    elif val > 2500: color = "\033[93m"
                elif name == "TMP" and isinstance(val, int):
                    if val > 105: color = "\033[91m"
                    elif val < 40: color = "\033[96m"
                    
                display.append(f" {name}: {color}{str(val):>4} {unit}\033[0m\033[1m |")
            
            # Print over the same line
            sys.stdout.write("\r" + "".join(display[:-1]) + "   ")
            sys.stdout.flush()
            
    except KeyboardInterrupt:
        print("\n\033[93mStopped by user.\033[0m")
    except Exception as e:
        print(f"\n\033[91mConnection Error: {e}\033[0m")
    finally:
        # Show cursor
        sys.stdout.write("\033[?25h")
        try: sock.close()
        except: pass

if __name__ == "__main__":
    main()
