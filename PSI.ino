#define ANALOG_INPUT A0
#define LED1_PIN 13
#define TOGGLE_LED '0'

bool led1_on = false;

void setup() {
  pinMode(LED1_PIN, OUTPUT);
  digitalWrite(LED1_PIN, LOW);
  Serial.begin(9600); 
}

void loop() {
  // Print the status of a0 to the console
  Serial.print("{ \"a0\": \"");
  Serial.print(analogRead(ANALOG_INPUT));
  Serial.println("\" }");
  delay(100);
}

// Listen for incomming messages over the serial console
void serialEvent() {
  while (Serial.available()) {
    char command = (char)Serial.read();
    if (command != '\n') {
      execute_command(command);
    }
  }
}

// Callback for the Serial Console
void execute_command(char command) {
  switch (command) {
    case TOGGLE_LED:
      toggle_led(LED1_PIN);
      break;
  }
}

void toggle_led(char pin) {
  if (led1_on) {
    digitalWrite(pin, LOW);
  }

  else {
    digitalWrite(pin, HIGH);
  }

  led1_on = !led1_on;
}
