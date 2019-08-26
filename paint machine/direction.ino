#define EN 8
#define X_DIR 5
#define Y_DIR 6
#define Z_DIR 7
#define X_STP 2
#define Y_STP 3
#define Z_STP 4

// Hàm điều khiển hướng và số bước của động cơ
void step(boolean dir, byte dirPin, byte stepperPin, int steps)
{
  digitalWrite(dirPin, dir);
  delay(50);
  for (int i = 0; i < steps; i++) {
    digitalWrite(stepperPin, HIGH);
    delayMicroseconds(800);  
    digitalWrite(stepperPin, LOW);
    delayMicroseconds(800);  
  }
}

void setup(){
  pinMode(X_DIR, OUTPUT);
  pinMode(X_STP, OUTPUT);
  pinMode(Y_DIR, OUTPUT); 
  pinMode(Y_STP, OUTPUT);
  pinMode(Z_DIR, OUTPUT);
  pinMode(Z_STP, OUTPUT);
  pinMode(EN, OUTPUT);
  digitalWrite(EN, LOW);
}

void loop(){
  step(false, X_DIR, X_STP, 200); // Motor quay 1 vòng, 200 bước theo trục Ox
  step(false, Y_DIR, Y_STP, 200); // Motor quay 1 vòng, 200 bước theo trục Oy
  step(false, Z_DIR, Z_STP, 200); // Motor quay 1 vòng, 200 bước theo trục Oz
  delay(1000);
  // Quay chiều ngược lại
  step(true, X_DIR, X_STP, 200); 
  step(true, Y_DIR, Y_STP, 200);
  step(true, Z_DIR, Z_STP, 200);
  delay(1000);
}