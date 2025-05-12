#include <Arduino_HTS221.h>

float wmatemp, wmahumidity;
float deltatemp = 0, deltahumidity = 0;
float readtemp, readhumidity;
float alpha = 0.5, beta = 0.8;
float epsilontemp = 1, epsilonhumidity = 3;
float expectedtemp, expectedhumidity;

float svalue(float prev, float next, float alpha) {
  return (1 - alpha) * prev + alpha * next;
}
float sdelta(float prev, float next, float beta) {
  return (1 - beta) * prev + beta * next;
}

void setup() {
  Serial.begin(9600);
  while (!Serial);

  if (!HTS.begin()) {
    Serial.println("Failed to initialize humidity temperature sensor!");
    while (1);
  }
  Serial.println("Initializing model...");
  // At the start, assume the average to be the first read and delta to be 0
  wmatemp = HTS.readTemperature();
  wmahumidity = HTS.readHumidity();
  delay(2000);
}

void loop() {
  // calculate expected values
  expectedtemp = wmatemp + deltatemp;
  expectedhumidity = wmahumidity + deltahumidity;
  // get new reads
  readtemp = HTS.readTemperature();
  readhumidity = HTS.readHumidity();
  Serial.println("Current temperature: " + String(readtemp, 2));
  Serial.println("Current humidity: " + String(readhumidity, 2));
  deltatemp = sdelta(deltatemp, readtemp - wmatemp, beta);
  wmatemp = svalue(wmatemp, readtemp, alpha);
  // compare new wma with expected
  if (abs(wmatemp - expectedtemp) > epsilontemp) {
    Serial.println("Temperature WMA: " + String(wmatemp, 2));
    Serial.println("Temperature delta: " + String(deltatemp, 2));
  }
  deltahumidity = sdelta(deltahumidity, readhumidity - wmahumidity, beta);
  wmahumidity = svalue(wmahumidity, readhumidity, alpha);
  if (abs(wmahumidity - expectedhumidity) > epsilonhumidity) {
    Serial.println("Humidity WMA: " + String(wmahumidity, 2));
    Serial.println("Humidity delta: " + String(deltahumidity, 2));
  }
  delay(2000);
}

