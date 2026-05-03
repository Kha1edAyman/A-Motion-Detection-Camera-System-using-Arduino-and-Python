/*
  ============================================================
  PIR Motion Sensor + SG90 Servo — Arduino Uno
  ============================================================
  Connections:
    PIR VCC  → 5V      PIR GND → GND     PIR OUT → D2
    Servo Red → 5V     Servo Brown → GND  Servo Yellow → D9
  ============================================================
*/

#include <Servo.h>

const int PIR_PIN   = 2;   // PIR output pin
const int SERVO_PIN = 9;   // Servo signal pin

Servo myServo;

int  pirState      = LOW;  // current PIR reading
int  lastPirState  = LOW;  // previous PIR reading
bool motionActive  = false;

const int SERVO_IDLE   = 0;    // degrees — resting position
const int SERVO_ACTIVE = 90;   // degrees — motion detected position
const unsigned long HOLD_TIME = 3000; // ms to hold servo after motion stops

unsigned long lastMotionTime = 0;

void setup() {
  Serial.begin(9600);
  pinMode(PIR_PIN, INPUT);
  myServo.attach(SERVO_PIN);
  myServo.write(SERVO_IDLE);

  // Warm-up delay for PIR sensor (10–60 s recommended, shortened for demo)
  Serial.println("=== PIR + Servo System Starting ===");
  Serial.println("Waiting for PIR sensor warm-up (5 s)...");
  delay(5000);
  Serial.println("Ready. Monitoring for motion...");
}

void loop() {
  pirState = digitalRead(PIR_PIN);

  // --- Motion DETECTED ---
  if (pirState == HIGH && lastPirState == LOW) {
    Serial.println("[EVENT] Motion DETECTED!");
    myServo.write(SERVO_ACTIVE);
    motionActive     = true;
    lastMotionTime   = millis();
  }

  // --- Motion CLEARED ---
  if (pirState == LOW && lastPirState == HIGH) {
    Serial.println("[EVENT] Motion cleared. Holding servo...");
    lastMotionTime = millis();
  }

  // --- Return servo to idle after hold time ---
  if (motionActive && pirState == LOW) {
    if (millis() - lastMotionTime >= HOLD_TIME) {
      Serial.println("[INFO] Returning servo to idle position.");
      myServo.write(SERVO_IDLE);
      motionActive = false;
    }
  }

  lastPirState = pirState;
  delay(50); // debounce / polling rate
}
