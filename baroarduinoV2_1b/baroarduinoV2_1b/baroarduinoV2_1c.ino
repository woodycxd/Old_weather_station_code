#include <SD.h>
#include <Wire.h>


int loopcount;
int sensorPin = 0;    // select the input pin for the potentiometer
int ledPin = 13;      // select the pin for the LED
int sensorValue = 0;// variable to store the value coming from the sensor
int temp_sensor=0;
int sensor_temp_pin=1;
int sensor_light_pin=2;
int dig_temp_pin=7;
int dig_light_pin = 6;
int sensor_light=0;
int pulse_pin=5;
unsigned long duration;

void setup() {
  Serial.begin(57600);
  Wire.begin();

  delay(1000);
  pinMode(dig_temp_pin,OUTPUT);
  pinMode(pulse_pin,INPUT);
  digitalWrite(dig_temp_pin,HIGH);
  pinMode(dig_light_pin,OUTPUT);
  digitalWrite(dig_light_pin,HIGH);
  
  pinMode(ledPin, OUTPUT);  
  

void loop() {
  // read the value from the sensor
  sensorValue = analogRead(sensorPin);
  temp_sensor=analogRead(sensor_temp_pin);
  sensor_light=analogRead(sensor_light_pin);
  duration=pulseIn(pulse_pin,HIGH);
 Serial.print(sensorValue);
  Serial.print(",");
  Serial.print(sensor_light);
  Serial.print(",");
  Serial.print(duration);
  Serial.print(",");
  Serial.print(temp_sensor);
 delay(59000);
delay(1000); 
 
                   
}
