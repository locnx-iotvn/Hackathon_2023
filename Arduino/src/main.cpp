#include <../lib/main.h>

boolean bPlayChess = false;

double L1 = 256;  //L1 = 255mm
double L2 = 244;  //L2 = 245mm
double theta1, theta2;

int stepper1Position, stepper2Position;

String content = "";
String dataFromUart[NUMBER_DATA_SERIAL];
int dataPlayChess[7];   // Status, Coordinates_X0, Coordinates_Y0, Coordinates_X1, Coordinates_Y1
uint8_t numberChessEat = 0;

void startSetup();
void resetPosition();
void readDataFromUart();
void playChess();
void moveChess(int Coordinates_X0, int Coordinates_Y0, int Coordinates_X1, int Coordinates_Y1);
void moveChessTest();
void moveChessTest2();
void caculateRotationAngle(int x, int y);
void moveMotor(double theta1_, double theta2_);
void takeChessPieces();
void dropChessPieces();
void controlServo(uint8_t uiAngle);
void readDataFromUartDemo();
void playChessDemo();
void moveChessDemo(int statusReset, double theta1_, double theta2_, double theta3_, double theta4_);

void setup() {
  startSetup();
}

void loop() {
  // readDataFromUart();

  // if (bPlayChess == true)
  // {
  //   playChess();
  //   bPlayChess = false;
  // }
  // takeChessPieces();
  // delay(1000);

  // moveChessTest();
  // takeChessPieces();
  // delay(1000);

  readDataFromUartDemo();

  if (bPlayChess == true)
  {
    playChessDemo();
    bPlayChess = false;
  }
}

void startSetup()
{
  // Setup baudrate for UART
  Serial.begin(9600);

  // Start step motor 1
  stepper1.setMaxSpeed(200);
  stepper1.setAcceleration(100);
  stepper1.setSpeed(80);
  stepper1.setAcceleration(80);

  // Start step motor 2
  stepper2.setMaxSpeed(200);
  stepper2.setAcceleration(100);
  stepper2.setSpeed(80);
  stepper2.setAcceleration(80);

  // Start servo motor
  myservo.attach(SERVO_PIN);
  controlServo(0);

  // Setup pin output for sucking motor
  pinMode(SUCKING_MOTOR_PIN, OUTPUT);

  // Setup pin output for valve
  pinMode(VALVE_PIN, OUTPUT);

  // Setup pinout for switch limit
  pinMode(LIMIT_SWITCH_X, INPUT_PULLUP);
  pinMode(LIMIT_SWITCH_Y, INPUT_PULLUP);

  resetPosition();
}

void resetPosition() {
  delay(100);
  // Homing step motor X
  while (digitalRead(LIMIT_SWITCH_X) != LIMIT_SWITCH_PRESS) {
    stepper1.setSpeed(-60);
    stepper1.runSpeed();
    stepper1.setCurrentPosition(0); // When limit switch pressed set position to 0 steps
  }
  delay(20);

  // Homing step motor Y
  while (digitalRead(LIMIT_SWITCH_Y) != LIMIT_SWITCH_PRESS) {
    stepper2.setSpeed(60);
    stepper2.runSpeed();
    stepper2.setCurrentPosition(0);
    // stepper2.setCurrentPosition(120);
  }
  delay(20);

  while (digitalRead(LIMIT_SWITCH_Y) != LIMIT_SWITCH_PRESS) {
    stepper2.setSpeed(10);
    stepper2.runSpeed();
    stepper2.setCurrentPosition(0);
  }

  while (digitalRead(LIMIT_SWITCH_X) != LIMIT_SWITCH_PRESS) {
    stepper1.setSpeed(-10);
    stepper1.runSpeed();
    stepper1.setCurrentPosition(0); // When limit switch pressed set position to 0 steps
  }
  delay(20);

  Serial.println("stepper1.currentPosition(): " + String(stepper1.currentPosition()));
  Serial.println("stepper2.currentPosition(): " + String(stepper2.currentPosition()));
}

void readDataFromUart()
{
  if (Serial.available()) {
    content = Serial.readString(); // Read the incomding data from Processing
    // Extract the data from the string and put into separate integer variables (data[] array)
    for (int i = 0; i < 7; i++) {
      int index = content.indexOf(","); // locate the first ","
      dataPlayChess[i] = atol(content.substring(0, index).c_str()); //Extract the number from start to the ","
      content = content.substring(index + 1); //Remove the number from the string
    }
    bPlayChess = true;
  }
}

void playChess()
{
  if (dataPlayChess[0] == 2)
  {
    Serial.println("Eat and move the chess");
    Serial.println("Step1: Eatting the chess from(" + String(dataPlayChess[3]) + "," + String(dataPlayChess[4]) + ") to (" + String(dataPlayChess[5]) + "," + String(dataPlayChess[6]) + ")");

    moveChess(dataPlayChess[3], dataPlayChess[4], dataPlayChess[5], dataPlayChess[6]);
    
    delay(200);

    Serial.println("Step2: Moving the chess from (" + String(dataPlayChess[1]) + "," + String(dataPlayChess[2]) + ") to (" + String(dataPlayChess[3]) + "," + String(dataPlayChess[4]) + ")");
    moveChess(dataPlayChess[1], dataPlayChess[2], dataPlayChess[3], dataPlayChess[4]);
  }

  // Move normal
  else if (dataPlayChess[0] == 3)
  {
    Serial.println("Moving the chess");
    Serial.println("Only moving the chess from (" + String(dataPlayChess[1]) + "," + String(dataPlayChess[2]) + ") to (" + String(dataPlayChess[3]) + "," + String(dataPlayChess[4]) + ")");
    moveChess(dataPlayChess[1], dataPlayChess[2], dataPlayChess[3], dataPlayChess[4]);
  }
}

void readDataFromUartDemo()
{
  if (Serial.available()) {
    content = Serial.readString(); // Read the incomding data from Processing
    // Extract the data from the string and put into separate integer variables (data[] array)
    for (int i = 0; i < 1; i++) {
      int index = content.indexOf(","); // locate the first ","
      dataPlayChess[i] = atol(content.substring(0, index).c_str()); //Extract the number from start to the ","
      content = content.substring(index + 1); //Remove the number from the string
    }
    bPlayChess = true;
  }
}

void playChessDemo()
{
  if (dataPlayChess[0] == 2)
  {
    Serial.println("Eat and move the chess");
    // Serial.println("Step1: Eatting the chess from(" + String(dataPlayChess[3]) + "," + String(dataPlayChess[4]) + ") to (" + String(dataPlayChess[5]) + "," + String(dataPlayChess[6]) + ")");

    moveChessDemo(0,76,-44,25,-43);
    
    delay(200);

    // Serial.println("Step2: Moving the chess from (" + String(dataPlayChess[1]) + "," + String(dataPlayChess[2]) + ") to (" + String(dataPlayChess[3]) + "," + String(dataPlayChess[4]) + ")");
    moveChessDemo(1,54,-29,76,-44);
  }

  // Move normal
  else if (dataPlayChess[0] == 3)
  {
    Serial.println("Moving the chess");
    // Serial.println("Only moving the chess from (" + String(dataPlayChess[1]) + "," + String(dataPlayChess[2]) + ") to (" + String(dataPlayChess[3]) + "," + String(dataPlayChess[4]) + ")");
    // moveChess(dataPlayChess[1], dataPlayChess[2], dataPlayChess[3], dataPlayChess[4]);
    moveChessDemo(1,44,-27,75,-35);
  }
}

void moveChess(int Coordinates_X0, int Coordinates_Y0, int Coordinates_X1, int Coordinates_Y1)
{
    // Move motor to the position of chess pieces 
    Serial.println("Step1: Move to the position of chess");
    caculateRotationAngle(Coordinates_X0, Coordinates_Y0);
    moveMotor(theta1, theta2);

    // Take the chess pieces
    Serial.println("Step2: Take the chess pieces");
    takeChessPieces();
  
    // Move chess pieces to next postion
    Serial.println("Step3: Move chess pieces to next postion");
    caculateRotationAngle(Coordinates_X1, Coordinates_Y1);
    moveMotor(theta1, theta2);

    // Drop the chess pieces
    Serial.println("Step4: Drop the chess pieces");
    dropChessPieces();

    // Drop the chess pieces
    Serial.println("Step5: Move to start position");
    resetPosition();
    // moveMotor(0, 0);
}

void moveChessTest()
{
  if (Serial.available()) {
    content = Serial.readString(); // Read the incomding data from Processing
    // Extract the data from the string and put into separate integer variables (data[] array)
    for (int i = 0; i < 4; i++) {
      int index = content.indexOf(","); // locate the first ","
      dataPlayChess[i] = atol(content.substring(0, index).c_str()); //Extract the number from start to the ","
      content = content.substring(index + 1); //Remove the number from the string
    }
    bPlayChess = true;
  }

  if (bPlayChess == true)
  {
    // Move motor to the position of chess pieces 
    Serial.println("Step1: Move to the position of chess");
    moveMotor(dataPlayChess[0], dataPlayChess[1]);
    Serial.print("theta11: "); Serial.println(dataPlayChess[0]);
    Serial.print("theta21: "); Serial.println(dataPlayChess[1]);

    // Take the chess pieces
    Serial.println("Step2: Take the chess pieces");
    // delay(2000);
    takeChessPieces();
  
    // Move chess pieces to next postion
    Serial.println("Step3: Move chess pieces to next postion");
    moveMotor(dataPlayChess[2], dataPlayChess[3]);
    Serial.print("theta11: "); Serial.println(dataPlayChess[2]);
    Serial.print("theta21: "); Serial.println(dataPlayChess[3]);
    // delay(2000);

    // Drop the chess pieces
    Serial.println("Step4: Drop the chess pieces");
    dropChessPieces();

    // Drop the chess pieces
    Serial.println("Step5: Move to start position");
    resetPosition();

    bPlayChess = false;
  }
}

void moveChessDemo(int statusReset, double theta1_, double theta2_, double theta3_, double theta4_)
{
    // Move motor to the position of chess pieces 
    Serial.println("Step1: Move to the position of chess");
    moveMotor(theta1_, theta2_);
    Serial.print("theta11: "); Serial.println(theta1_);
    Serial.print("theta21: "); Serial.println(theta2_);

    // Take the chess pieces
    Serial.println("Step2: Take the chess pieces");
    takeChessPieces();
  
    // Move chess pieces to next postion
    Serial.println("Step3: Move chess pieces to next postion");
    moveMotor(theta3_, theta4_);
    Serial.print("theta11: "); Serial.println(theta3_);
    Serial.print("theta21: "); Serial.println(theta4_);

    // Drop the chess pieces
    Serial.println("Step4: Drop the chess pieces");
    dropChessPieces();

    // Drop the chess pieces
    if(statusReset == 1)
    {
      Serial.println("Step5: Move to start position");
      resetPosition();
    }

}

void caculateRotationAngle(int x, int y) {
  theta2 = acos((pow(x,2) + pow(y,2) - pow(L1,2) - pow(L2,2)) / (2 * L1 * L2));
  if (x < 0 && y < 0) {
    theta2 = (-1) * theta2;
  }
  
  theta1 = atan(x / y) - atan((L2 * sin(theta2)) / (L1 + L2 * cos(theta2)));
  theta2 = (-1) * theta2 * 180 / PI;
  theta1 = theta1 * 180 / PI;
   
 // Angles adjustment depending in which quadrant the final tool coordinate x,y is
  if (x >= 0 && y >= 0) {       // 1st quadrant
    theta1 = 90 - theta1;
  }
  if (x < 0 && y > 0) {       // 2nd quadrant
    theta1 = 90 - theta1;
  }
  if (x < 0 && y < 0) {       // 3d quadrant
    theta1 = 270 - theta1;
  }
  if (x > 0 && y < 0) {       // 4th quadrant
    theta1 = -90 - theta1;
  }
  if (x < 0 && y == 0) {
    theta1 = 270 + theta1;
  }

  theta2 = theta2 + 69;

  theta1=round(theta1);
  theta2=round(theta2);
  
  Serial.print("theta1: "); Serial.println(theta1);
  Serial.print("theta2: "); Serial.println(theta2);
}

void convertCoordinatesToAngle(int x, int y) {
  Serial.print("theta1: "); Serial.println(theta1);
  Serial.print("theta2: "); Serial.println(theta2);
}

void moveMotor(double theta1_, double theta2_)
{
  stepper1Position = theta1_ * NUMBER_STEP_ONCE_CYCLE / 360;
  stepper2Position = theta2_ * NUMBER_STEP_ONCE_CYCLE / 360;

  stepper1.moveTo(stepper1Position);
  stepper2.moveTo(stepper2Position);

  while (stepper1.currentPosition() != stepper1Position || stepper2.currentPosition() != stepper2Position) {
    stepper1.run();
    stepper2.run();
  }

  delay(300);
}

void takeChessPieces()
{
  // Thả ông hút xuống
  controlServo(180);
  
  // Bắt đầu hút quần cờ, bật máy hút
  digitalWrite(SUCKING_MOTOR_PIN, HIGH);
  delay(500); 
  digitalWrite(SUCKING_MOTOR_PIN, LOW); 

  // Nhắc ống hút + quân cờ
  controlServo(0);
}

void dropChessPieces()
{
  // Thả ông hút xuống
  controlServo(180);
  
  // Bắt đầu thả quần cờ, bật van
  digitalWrite(VALVE_PIN, HIGH); 
  delay(1000); 

    // Nhắc ống hút lên
  controlServo(0);

  // Bắt đầu thả tắt van
  digitalWrite(VALVE_PIN, LOW); 
  // controlServo(0);
}

void controlServo(uint8_t uiAngle)
{
  myservo.write(uiAngle);
  delay(1000); 
}