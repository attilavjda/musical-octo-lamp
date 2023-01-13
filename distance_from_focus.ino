#include <math.h>

const float fx = 0.0; // x-coordinate of focus
const float fy = -2.0; // y-coordinate of focus
const float p = 4.0; // distance between focus and directrix

float x, y, distance, threshold;
int potPin = A0;
int ledPin = 13;


void setup() {
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  int potValue = analogRead(potPin); // read position from potentiometer
  x = potValue;
  y = (x*x) / (4.0*p); // calculate y-coordinate of point on parabola
  distance = sqrt((x - fx) * (x - fx) + (y - fy) * (y - fy)); // distance formula
  if (distance <= 4) { // if distance is close enough to focus
    digitalWrite(ledPin, HIGH); // turn on LED
  } else {
    digitalWrite(ledPin, LOW); // turn off LED
  }
  delay(200);
}