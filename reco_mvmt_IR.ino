int sensor = 7;
int val = 0;
void setup() {
  Serial.begin(9600);
  // put your setup code here, to run once:
  pinMode(sensor, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  val = digitalRead(sensor);
  Serial.println(val);
  delay(500);
}
