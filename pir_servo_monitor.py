"""
============================================================
PIR + Servo Monitor — Python Serial Reader
============================================================
Reads Arduino serial output, logs events with timestamps,
and can optionally send commands back to Arduino.

Requirements:
    pip install pyserial

Usage:
    python pir_servo_monitor.py
    python pir_servo_monitor.py --port COM3          # Windows
    python pir_servo_monitor.py --port /dev/ttyUSB0  # Linux/Mac
    python pir_servo_monitor.py --port /dev/ttyUSB0 --baud 9600
============================================================
"""

import serial
import serial.tools.list_ports
import argparse
import time
import sys
from datetime import datetime


# ─── CONFIG ────────────────────────────────────────────────
DEFAULT_BAUD = 9600
LOG_FILE     = "pir_log.txt"
# ────────────────────────────────────────────────────────────


def list_ports():
    """Print all available serial ports."""
    ports = list(serial.tools.list_ports.comports())
    if not ports:
        print("No serial ports found.")
    else:
        print("Available ports:")
        for p in ports:
            print(f"  {p.device:15s} — {p.description}")


def find_arduino_port():
    """Auto-detect most likely Arduino port."""
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        desc = p.description.lower()
        if any(k in desc for k in ["arduino", "ch340", "cp210", "ftdi", "usb serial"]):
            return p.device
    # Fall back to first available port
    if ports:
        return ports[0].device
    return None


def monitor(port: str, baud: int, log_path: str):
    """Open serial connection and monitor events."""
    print(f"\n{'='*55}")
    print(f"  PIR + Servo Monitor")
    print(f"  Port: {port}   Baud: {baud}")
    print(f"  Log : {log_path}")
    print(f"{'='*55}")
    print("  Press Ctrl+C to stop.\n")

    motion_count = 0
    session_start = datetime.now()

    try:
        ser = serial.Serial(port, baud, timeout=1)
        time.sleep(2)  # Wait for Arduino reset after connection
        ser.reset_input_buffer()

        with open(log_path, "a", encoding="utf-8") as log:
            log.write(f"\n--- Session started {session_start.isoformat()} ---\n")

            while True:
                if ser.in_waiting:
                    raw = ser.readline()
                    try:
                        line = raw.decode("utf-8").strip()
                    except UnicodeDecodeError:
                        continue

                    if not line:
                        continue

                    ts = datetime.now().strftime("%H:%M:%S.%f")[:-3]
                    tag = classify(line)

                    # Console output with color codes
                    color = {
                        "MOTION": "\033[92m",   # green
                        "CLEAR" : "\033[94m",   # blue
                        "INFO"  : "\033[93m",   # yellow
                        "SYSTEM": "\033[96m",   # cyan
                        "OTHER" : "\033[0m",
                    }.get(tag, "\033[0m")

                    print(f"{color}[{ts}] {line}\033[0m")
                    log.write(f"[{ts}] [{tag}] {line}\n")
                    log.flush()

                    if tag == "MOTION":
                        motion_count += 1
                        print(f"  \033[92m→ Motion event #{motion_count}\033[0m")

    except serial.SerialException as e:
        print(f"\n[ERROR] Serial error: {e}")
        print("  Check the port and that Arduino is connected.\n")
        sys.exit(1)
    except KeyboardInterrupt:
        elapsed = datetime.now() - session_start
        print(f"\n\n{'='*55}")
        print(f"  Session ended after {str(elapsed).split('.')[0]}")
        print(f"  Total motion events : {motion_count}")
        print(f"  Log saved to        : {log_path}")
        print(f"{'='*55}\n")


def classify(line: str) -> str:
    """Categorise a serial line for display and logging."""
    low = line.lower()
    if "detected" in low:
        return "MOTION"
    if "cleared" in low or "idle" in low:
        return "CLEAR"
    if "[info]" in low or "returning" in low:
        return "INFO"
    if "starting" in low or "ready" in low or "warm" in low:
        return "SYSTEM"
    return "OTHER"


def main():
    parser = argparse.ArgumentParser(description="PIR + Servo Arduino Monitor")
    parser.add_argument("--port", "-p", help="Serial port (e.g. COM3 or /dev/ttyUSB0)")
    parser.add_argument("--baud", "-b", type=int, default=DEFAULT_BAUD, help="Baud rate (default 9600)")
    parser.add_argument("--list", "-l", action="store_true", help="List available serial ports and exit")
    parser.add_argument("--log",  default=LOG_FILE, help=f"Log file path (default: {LOG_FILE})")
    args = parser.parse_args()

    if args.list:
        list_ports()
        return

    port = args.port
    if not port:
        port = find_arduino_port()
        if port:
            print(f"Auto-detected port: {port}")
        else:
            print("[ERROR] No serial port found. Use --list to see available ports.")
            sys.exit(1)

    monitor(port, args.baud, args.log)


if __name__ == "__main__":
    main()
