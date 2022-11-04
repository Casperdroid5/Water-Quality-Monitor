
// defines pins numbers
const int stepPin = 3;
const int dirPin = 2;

void setup() {
  // Sets the two pins as Outputs
  pinMode(stepPin, OUTPUT);
  pinMode(dirPin, OUTPUT);
}
void loop() {
  digitalWrite(dirPin, HIGH); // Enables the motor to move in a particular direction
  // Makes 500 pulses for making one full cycle rotation
  for (int x = 0; x < 1000; x++) {
    digitalWrite(stepPin, HIGH);
    delayMicroseconds(100); //1000 for 24V stepper, 500 for 12V stepper
    digitalWrite(stepPin, LOW);
    delayMicroseconds(100); //1000 for 24V stepper, 500 for 12V stepper 
  }
}
