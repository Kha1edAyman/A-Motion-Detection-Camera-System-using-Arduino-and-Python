int pirPin = 2;
int motionState = 0;

void setup() {
  pinMode(pirPin, INPUT);
  Serial.begin(9600);
}

void loop() {
  motionState = digitalRead(pirPin);

  if (motionState == HIGH) {
    Serial.println("MOTION_DETECTED");
    delay(2000);
  }
}