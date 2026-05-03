# A-Motion-Detection-Camera-System-using-Arduino-and-Python

This project is a simple motion detection system using a PIR sensor connected to Arduino. 
When motion is detected, a signal is sent to a Python script running on a computer, 
which then captures an image using a webcam. 
The system can be used for basic security, automation, or smart monitoring applications.

# project Circuit Diagram

<img width="968" height="666" alt="Screenshot 2026-05-03 at 11 16 05 AM" src="https://github.com/user-attachments/assets/f9b47851-e8d8-4e12-937b-03ad4a1f18b1" />

# project image 1


<img width="1200" height="1600" alt="photo1" src="https://github.com/user-attachments/assets/3d7181f1-eb89-47ce-9a98-b618208cea50" />

# project image 2


<img width="1200" height="1600" alt="photo2" src="https://github.com/user-attachments/assets/9244f142-e676-43bc-9bc2-6bf36c3eebc2" />

### Connections:
- PIR VCC → Arduino 5V  
- PIR GND → Arduino GND  
- PIR OUT → Arduino Pin 2


# How to Use

### 1 — Wire the circuit
Connect everything exactly as shown in the diagram above. PIR pins: VCC → 5V, GND → GND, OUT → D2. Servo wires: red → 5V, brown → GND, yellow → D9. Then plug the Arduino into your laptop via USB.
### 2 — Upload the Arduino code
Open pir_servo.ino in the Arduino IDE, select board Arduino Uno and the correct COM port from Tools menu, then click Upload. Open Serial Monitor (baud 9600) — you'll see "Ready. Monitoring for motion..." after the 5-second warm-up.
### 3 — Install Python dependency
In your terminal run pip install pyserial. This is the only external library needed.
### 4 — Run the Python monitor
Close the Arduino Serial Monitor first (only one program can use the port at a time), then run the Python script. It auto-detects the Arduino port, but you can specify it manually if needed:
bashpython pir_servo_monitor.py                        # auto-detect
python pir_servo_monitor.py --port COM3            # Windows
python pir_servo_monitor.py --port /dev/ttyUSB0   # Linux / Mac
python pir_servo_monitor.py --list                 # see all ports
### 5 — Test it
Wave your hand in front of the PIR dome — the servo rotates to 90°, the terminal prints a green MOTION DETECTED message, and the event is logged to pir_log.txt with a timestamp. When motion stops, the servo holds for 3 seconds then returns to 0°.
### 6 — Tune if needed
In the .ino file you can change HOLD_TIME (how long servo stays active after motion stops), SERVO_IDLE and SERVO_ACTIVE angles, or the warm-up delay at startup. The PIR module itself also has two small potentiometers on the back — one adjusts sensitivity, the other adjusts the detection hold time at hardware level.

