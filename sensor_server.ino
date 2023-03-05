#include <dummy.h>
#include <Arduino.h>
#include <WiFi.h>
#include <WiFiClient.h>
#include <WiFiAP.h>
#define SOUND_SPEED 0.034

const int sensor = 4;              // the pin that the sensor is atteched to
const int usonic = 23;
int state = LOW;             // by default, no motion detected
int val = 0;                 // variable to store the sensor status (value)
const int trigPin = 17;
const int motor = 19;

long duration;
double distanceCm;
float angleWait;
uint64_t key1, key2, key3, key4;

WiFiServer server(80);

void setup() {
  pinMode(usonic, INPUT);      // initalize usonic as an input
  pinMode(sensor, INPUT);    // initialize sensor as an input
  pinMode(trigPin, OUTPUT); // Sets the trigPin as an Output
  pinMode(motor, OUTPUT);
  Serial.begin(9600);        // initialize serial

  if (!WiFi.softAP("inf network", "potatoes")) {
    Serial.println("Soft AP creation failed.");
    while(1);
  }
  IPAddress myIP = WiFi.softAPIP();
  Serial.print("AP IP address: ");
  Serial.println(myIP);
  server.begin();

  Serial.println("Server started");

  // generate keys
  key1 = 0xAAAAAAAA;
  key2 = 0x55555555;
}

void loop(){
  WiFiClient client = server.available();

  val = digitalRead(sensor);   // read sensor value
  if (val == HIGH) {           // check if the sensor is HIGH
    // Clears the trigPin
    digitalWrite(trigPin, LOW);
    delayMicroseconds(2);
    // Sets the trigPin on HIGH state for 10 micro seconds
    digitalWrite(trigPin, HIGH);
    delayMicroseconds(10);
    digitalWrite(trigPin, LOW);
    duration = pulseIn(usonic, HIGH);
    Serial.print("Duration: ");
    Serial.println(duration);
    distanceCm = duration * SOUND_SPEED/2;
    Serial.print("Distance (cm): ");
    Serial.println(distanceCm);
    digitalWrite(motor, HIGH);
    angleWait = abs(cos(distanceCm + random(-1000, 1000))) + 1.0;
    Serial.println(angleWait);
    delay(angleWait);
    digitalWrite(motor, LOW);
    
    if (state == LOW) {
      Serial.println("Motion detected!"); 
      state = HIGH;       // update variable state to HIGH
    }
  } 
  else {      
    if (state == HIGH){
      Serial.println("Motion stopped!");
      state = LOW;       // update variable state to LOW
    }
    delay(100);
  }

  if (client) {
    String currentLine = "";
    while (client.connected()) {            // loop while the client's connected
      if (client.available()) {             // if there's bytes to read from the client,
        char c = client.read();             // read a byte, then
        if (c == '\n') {                    // if the byte is a newline character

          // if the current line is blank, you got two newline characters in a row.
          // that's the end of the client HTTP request, so send a response:
          if (currentLine.length() == 0) {
            // HTTP headers always start with a response code (e.g. HTTP/1.1 200 OK)
            // and a content-type so the client knows what's coming, then a blank line:
            client.println("HTTP/1.1 200 OK");
            client.println("Content-type:text/plain");
            client.println();

            // the content of the HTTP response follows the header:
            client.print((uint64_t) distanceCm | key1, 16);
            client.print("\n");
            client.print((uint64_t) distanceCm & key1, 16);
            client.print("\n");
            client.print((uint64_t) distanceCm | key2, 16);
            client.print("\n");
            client.print((uint64_t) distanceCm & key2, 16);

            // The HTTP response ends with another blank line:
            client.println();
            // break out of the while loop:
            break;
          } else {    // if you got a newline, then clear currentLine:
            currentLine = "";
          }
        } else if (c != '\r') {  // if you got anything else but a carriage return character,
          currentLine += c;      // add it to the end of the currentLine
        }
      }
    }
    // close the connection:
    client.stop();
    Serial.println("Client Disconnected.");
  }
}