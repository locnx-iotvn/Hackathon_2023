#include <../lib/main.h>

boolean bPlayChess = false;

double L1 = 256;  //L1 = 255mm
double L2 = 244;  //L2 = 245mm
double theta1, theta2;

int stepper1Position, stepper2Position;

String content = "";
String dataFromUart[NUMBER_DATA_SERIAL];
int dataPlayChess[5];   // Status, Coordinates_X0, Coordinates_Y0, Coordinates_X1, Coordinates_Y1
int dataPlayChess_Bk[5];   // Status, Coordinates_X0, Coordinates_Y0, Coordinates_X1, Coordinates_Y1
uint8_t numberChessEat = 0;

void startSetup();
void resetPosition();
void readDataFromUart();\
void convertDataUartToCoordinates();
void playChess();
void moveChess(int Coordinates_X0, int Coordinates_Y0, int Coordinates_X1, int Coordinates_Y1);
void caculateRotationAngle(int x, int y);
void moveMotor(double theta1_, double theta2_);
void takeChessPieces();
void dropChessPieces();
void controlServo(uint8_t uiAngle);

void setup() {
  startSetup();
}

void loop() {
    if (digitalRead(LIMIT_SWITCH_X) != LIMIT_SWITCH_PRESS)
    {
      Serial.println("digitalRead(LIMIT_SWITCH_X)");
    }
    if (digitalRead(LIMIT_SWITCH_Y) != LIMIT_SWITCH_PRESS)
    {
      Serial.println("digitalRead(LIMIT_SWITCH_Y)");
    }    
    delay(1000);

  // Read data
  // readDataFromUart();

  // if (bPlayChess == true)
  // {
  //   playChess();
  //   bPlayChess = false;
  // }
}

void startSetup()
{
  // Setup baudrate for UART
  Serial.begin(9600);

  // Start step motor 1
  stepper1.setMaxSpeed(4000);
  stepper1.setAcceleration(2000);
  // stepper1.setSpeed(100);
  // stepper1.setAcceleration(100);

  // Start step motor 2
  stepper2.setMaxSpeed(4000);
  stepper2.setAcceleration(2000);
  // stepper2.setSpeed(100);
  // stepper2.setAcceleration(100);

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
  delay(500);
  // Homing step motor X
  while (digitalRead(LIMIT_SWITCH_X) != LIMIT_SWITCH_PRESS) {
    stepper1.setSpeed(-130);
    stepper1.runSpeed();
    // stepper1.setCurrentPosition(2000); // When limit switch pressed set position to 0 steps
  }
  delay(20);

  // stepper1.moveTo(0);
  // while (stepper1.currentPosition() != 0) {
  //   stepper1.run();
  // }

  // Homing step motor Y
  while (digitalRead(LIMIT_SWITCH_Y) != LIMIT_SWITCH_PRESS) {
    stepper2.setSpeed(130);
    stepper2.runSpeed();
    // stepper1.setCurrentPosition(100);
  }

  while (digitalRead(LIMIT_SWITCH_Y) != LIMIT_SWITCH_PRESS) {
    stepper2.setSpeed(20);
    stepper2.runSpeed();
    // stepper1.setCurrentPosition(100);
  }

  while (digitalRead(LIMIT_SWITCH_X) != LIMIT_SWITCH_PRESS) {
    stepper1.setSpeed(-20);
    stepper1.runSpeed();
    // stepper1.setCurrentPosition(2000); // When limit switch pressed set position to 0 steps
  }
  delay(20);

  // stepper2.moveTo(0);
  // while (stepper2.currentPosition() != 0) {
  //   stepper2.run();
  // }
}

void readDataFromUart()
{
  if (Serial.available()) {
    content = Serial.readString(); // Read the incomding data from Processing
    for (int i = 0; i < NUMBER_DATA_SERIAL; i++) {
      int index = content.indexOf(","); // locate the first ","
      dataFromUart[i] = content.substring(0, index);
      content = content.substring(index + 1); //Remove the number from the string
      Serial.println(dataFromUart[i]);
    }

    /*
     data[0] - status 
     data[1] - XY1 position
     data[2] - XY2 position
    */

    bPlayChess = true;
  }
}

void convertDataUartToCoordinates()
{
  char dataFromUart_temp[3];
  char posstionChess_temp[3];
  strcpy(dataFromUart_temp, dataFromUart[0].c_str());

  // Convert Uart data to chess playing data
  Serial.println(dataFromUart[0]);
  dataPlayChess[0] = atol(dataFromUart[0].c_str());

  // Coordinates X of the chess
  for (int i = 0; i < NUMBER_POSTION_CHESS; ++i) {
    strcpy(posstionChess_temp, posstionChess[i].c_str());
    if ((dataFromUart_temp[0] == posstionChess_temp[0]) && (dataFromUart_temp[1] == posstionChess_temp[1]) && (dataFromUart_temp[2] == posstionChess_temp[2]))
    // if (posstionChess[i] == dataFromUart[1])
    {
      dataPlayChess[1] = coordinatesChess[i][0];
      dataPlayChess[2] = coordinatesChess[i][1];
      Serial.println(i);
      break;
    }
  }
  Serial.println(dataFromUart[0]);

  // // Coordinates Y of the chess
  // for (int i = 0; i < NUMBER_POSTION_CHESS; ++i) {
  //   if (posstionChess[i] == dataFromUart[2])
  //   {
  //     dataPlayChess[3] = coordinatesChess[i][0];
  //     dataPlayChess[4] = coordinatesChess[i][1];
  //     Serial.println(i);
  //     break;
  //   }
  // }
  // Serial.println(dataFromUart[0]);
}

void playChess()
{
  convertDataUartToCoordinates();
  // Eat chess and move chess
  if (dataPlayChess[0] == 2)
  {
    Serial.println("Eat and move the chess");
    Serial.println("Step1: Eatting the chess");
    // moveChess(dataPlayChess[3], dataPlayChess[4], coordinatesChessEat[numberChessEat][0], coordinatesChessEat[numberChessEat][1]);
    // numberChessEat++;
    
    // delay(200);

    // Serial.print("Step2: Moving the chess");
    // moveChess(dataPlayChess[1], dataPlayChess[2], dataPlayChess[3], dataPlayChess[4]);
  // }
  // // Move normal
  // else if (dataPlayChess[0] == 2)
  // {
  //   Serial.print("Only move the chess");
  //   moveChess(dataPlayChess[1], dataPlayChess[2], dataPlayChess[3], dataPlayChess[4]);
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
    // resetPosition();
    moveMotor(0, 0);
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

  theta2 = theta2 - 90;

  theta1=round(theta1);
  theta2=round(theta2);
  
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