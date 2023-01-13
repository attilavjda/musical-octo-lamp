float a = 0.5; // coefficient of x^2
float h = 5.0; // x-coordinate of the vertex
float k = 2.0; // y-coordinate of the vertex
float p = 3.0; // distance from vertex to focus

void setup() {
  Serial.begin(9600);
}

void loop() {
  float x = analogRead(A0); // read x-coordinate from photoresistor
  float y = a * (x - h) * (x - h) + k; // calculate y-coordinate on parabola
  float fx = h; // x-coordinate of focus
  float fy = k + p; // y-coordinate of focus
  float distance = sqrt((x - fx) * (x - fx) + (y - fy) * (y - fy)); // distance formula
  Serial.println(distance); // print distance to focus
  delay(100);
}