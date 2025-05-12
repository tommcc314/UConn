#include <Arduino_LSM9DS1.h>
float wmax, wmay, z;
float deltax = 0, deltay = 0;
float readx, ready;
float alpha = 0.5, beta = 0.8;
float epsilonx = 10, epsilony = 10;
float expectedx, expectedy;

float svalue(float prev, float next, float alpha) {
  return (1 - alpha) * prev + alpha * next;
}
float sdelta(float prev, float next, float beta) {
  return (1 - beta) * prev + beta * next;
}

void setup() {
  Serial.begin(9600);
  while (!Serial);
  Serial.println("Started");

  if (!IMU.begin()) {
    Serial.println("Failed to initialize IMU!");
    while (1);
  }
  Serial.println("Initializing model...");
  // At the start, assume the average to be the first read and delta to be 0
  IMU.readAcceleration(readx, ready, z);
  readx *= 100, ready *= 100;
  // The map function re-maps a number from one range to another
  wmax = map(readx, -97, 97, -90, 90);
  wmay = map(ready, -100, 100, -90, 90);
  delay(2000);
}

void loop() {
  // calculate expected values
  expectedx = wmax + deltax;
  expectedy = wmay + deltay;
  // get new reads
  IMU.readAcceleration(readx, ready, z);
  readx *= 100, ready *= 100;
  deltax = sdelta(deltax, readx - expectedx, beta);
  wmax = svalue(wmax, readx, alpha);
  deltay = sdelta(deltay, ready - expectedy, beta);
  wmay = svalue(wmay, ready, alpha);
  // compare new wma with expected
  if (abs(wmax - expectedx) > epsilonx || abs(wmay - expectedy) > epsilony) {
    Serial.print("Tilt WMA: ");
    if (wmax < 0) Serial.print("Down " + String(-wmax, 2) + " degrees, ");
    else Serial.print("Up " + String(wmax, 2) + " degrees, ");
    if (wmay < 0) Serial.println("Right " + String(-wmay, 2) + " degrees");
    else Serial.println("Left " + String(wmay, 2) + " degrees");
    Serial.print("Tilt delta: ");
    if (deltax < 0) Serial.print("Down " + String(-deltax, 2) + " degrees, ");
    else Serial.print("Up " + String(deltax, 2) + " degrees, ");
    if (deltay < 0) Serial.println("Right " + String(-deltay, 2) + " degrees");
    else Serial.println("Left " + String(deltay, 2) + " degrees");
  }
  delay(2000);
}
