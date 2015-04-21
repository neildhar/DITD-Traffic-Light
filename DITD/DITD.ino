void setup() {
    Serial.begin(9600);
    pinMode(6, INPUT);
}

void loop() {
  if(digitalRead(6)==LOW){
      delay(4000);
      Serial.println("This is high");
      delay(5000);
  }
}
