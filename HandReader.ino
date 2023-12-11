void setup() {
    Serial.begin(9600);
}

void loop() {
    // Your code to generate output
    int thumbSensor = analogRead(33);
    int indexSensor = analogRead(32);
    int middleSensor = analogRead(27);
    int ringSensor = analogRead(4);
    int pinkySensor = analogRead(12);
    int wristSensor  = analogRead(25);

    
    // Send the output over serial
    Serial.print(thumbSensor);
    Serial.print(" ")
    Serial.print(indexSensor);
    Serial.print(" ")
    Serial.print(middleSensor);
    Serial.print(" ")
    Serial.print(ringSensor);
    Serial.print(" ")
    Serial.print(pinkySensor);
    Serial.print(" ")
    Serial.println(wristSensor);
    

    delay(1000);
}
