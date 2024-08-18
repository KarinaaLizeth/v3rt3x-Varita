#include <Wire.h>
#include "GY521.h"

// Definir pines
const int buttonPin = 3; // GPIO3 para S3 Mini
const int ledPin = 5;    // GPIO5 para S3 Mini

GY521 sensor(0x68); // Dirección del sensor GY521 (MPU6050) en el bus I2C
bool buttonState = HIGH;
bool lastButtonState = HIGH;
bool capturing = false;
int sampleCount = 0;

// Función para leer datos del sensor GY521
void readGY521() {
  sensor.read();
  int16_t ax = sensor.getAccelX() *100;
  int16_t ay = sensor.getAccelY() *100;
  int16_t az = sensor.getAccelZ() *100;
  int16_t gx = sensor.getGyroX() *100;
  int16_t gy = sensor.getGyroY() *100;
  int16_t gz = sensor.getGyroZ() *100;

  Serial.print("DATA,");
  Serial.print(ax); Serial.print(",");
  Serial.print(ay); Serial.print(",");
  Serial.print(az); Serial.print(",");
  Serial.print(gx); Serial.print(",");
  Serial.print(gy); Serial.print(",");
  Serial.println(gz);
}

void setup() {
  Serial.begin(115200);
  Wire.begin(); // Iniciar el bus I2C

  pinMode(buttonPin, INPUT_PULLUP);
  pinMode(ledPin, OUTPUT);

  // Iniciar y verificar la conexión con el sensor
  if (sensor.wakeup() == false) {
    Serial.println("Error al conectar el GY521.");
    while (1);
  }
  Serial.println("GY521 conectado correctamente.");

  // Configurar la sensibilidad (opcional, puede ajustarse según sea necesario)
  sensor.setAccelSensitivity(3);  // Ajustar la sensibilidad del acelerómetro (0, 1, 2, 3)
  sensor.setGyroSensitivity(3);   // Ajustar la sensibilidad del giroscopio (0, 1, 2, 3)
}

void loop() {
  buttonState = digitalRead(buttonPin);

  if (buttonState == LOW && lastButtonState == HIGH) {
    capturing = !capturing;
    if (capturing) {
      Serial.println("CAPTURE_START");
      digitalWrite(ledPin, HIGH);
      sampleCount = 0;
    } else {
      Serial.println("CAPTURE_COMPLETE");
      digitalWrite(ledPin, LOW);
    }
    delay(200); 
  }

  if (capturing) {
    if (sampleCount < 40) {
      readGY521();
      sampleCount++;
    } else {
      Serial.println("CAPTURE_COMPLETE");
      capturing = false;
      digitalWrite(ledPin, LOW);
    }
    delay(50); 
  }

  lastButtonState = buttonState;
}
