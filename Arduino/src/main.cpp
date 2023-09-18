#include <Arduino.h>
#include <AccelStepper.h>
#include <Servo.h>
#include <math.h>

#define NUMBER_STEP_ONCE_CYCLE 600    // Dộng cơ bước NEMA 17 có thông số 200 bước/vòng
#define SERVO_PIN 9


// Define the stepper motors and the pins the will use
AccelStepper stepper1(1, 2, 5); // (Type:driver, STEP, DIR)
AccelStepper stepper2(1, 3, 6);

// Create servo object to control a servo
Servo myservo;  

boolean bControlMotor = false;

double L1 = 256;  //L1 = 255mm
double L2 = 244;  //L2 = 245mm
double theta1, theta2;

int stepper1Position, stepper2Position;

String content = "";
int data[5];

void resetPosition();
void caculateRotationAngle(float x, float y);
void readDataFromUart();
void moveMotor(double theta1_, double theta2_);
void takeChessPieces();
void dropChessPieces();
void controlServo(uint8_t uiAngle);

void setup() {
  Serial.begin(9600);

  // Stepper motors max speed
  stepper1.setMaxSpeed(4000);
  stepper1.setAcceleration(2000);
  stepper2.setMaxSpeed(4000);
  stepper2.setAcceleration(2000);

  stepper1.setSpeed(100);
  stepper2.setSpeed(100);
  stepper1.setAcceleration(100);
  stepper2.setAcceleration(100);

  myservo.attach(SERVO_PIN);  // attaches the servo on pin 9 to the servo object
  // gripperServo.attach(A0, 600, 2500);
  // // initial servo value - open gripper
  // data[6] = 180;
  // gripperServo.write(data[6]);
  // delay(1000);
  // data[5] = 100;
  // resetPosition();
}

void loop() {

  // Read data
  readDataFromUart();

  if ( bControlMotor == true)
  {
    // Move motor to the position of chess pieces 
    Serial.println("Step1: Move motor to the position of chess pieces");
    caculateRotationAngle(data[0], data[1]);
    moveMotor(theta1, theta2);
    // moveMotor(data[0], data[1]);

    // Take the chess pieces
    Serial.println("Step2: Take the chess pieces");
    takeChessPieces();
  
    // Move chess pieces to next postion
    Serial.println("Step3: Move chess pieces to next postion");
    caculateRotationAngle(data[2], data[3]);
    moveMotor(theta1, theta2);
    // moveMotor(data[2], data[3]);

    // Drop the chess pieces
    Serial.println("Step4: Drop the chess pieces");
    dropChessPieces();

    // Drop the chess pieces
    Serial.println("Step5: Move to start position");
    moveMotor(0, 0);

    bControlMotor = false;
  }

}

void resetPosition() {
  stepper1.moveTo(0);
  stepper2.moveTo(0);

  while (stepper1.currentPosition() != stepper1Position || stepper2.currentPosition() ) {
    stepper1.run();
    stepper2.run();
  }

  // Homing Stepper1
  // while (digitalRead(limitSwitch1) != 1) {
  //   stepper1.setSpeed(-1200);
  //   stepper1.runSpeed();
  //   stepper1.setCurrentPosition(-3955); // When limit switch pressed set position to 0 steps
  // }
  // delay(20);
  // stepper1.moveTo(0);
  // while (stepper1.currentPosition() != 0) {
  //   stepper1.run();
  // }

}

void caculateRotationAngle(float x, float y) {
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

void readDataFromUart()
{
  if (Serial.available()) {
    content = Serial.readString(); // Read the incomding data from Processing
    // Extract the data from the string and put into separate integer variables (data[] array)
    for (int i = 0; i < 5; i++) {
      int index = content.indexOf(","); // locate the first ","
      data[i] = atol(content.substring(0, index).c_str()); //Extract the number from start to the ","
      content = content.substring(index + 1); //Remove the number from the string
    }
    Serial.print("Move from (" + String(data[0]) + "," + String(data[1]) + ") to (" + String(data[3]) + "," + String(data[4]) + ")");
    bControlMotor = true;
    /*
     data[0] - X1 position
     data[1] - Y1 position
     data[2] - X2 position
     data[3] - Y2 position
    */
  }
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
  delay(1000); 

  // Nhắc ống hút + quân cờ
  controlServo(0);
}

void dropChessPieces()
{
  // Thả ông hút xuống
  controlServo(180);
  
  // Bắt đầu thả quần cờ, tắt máy hút
  delay(1000); 

  // Nhắc ống hút lên
  controlServo(0);
}

void controlServo(uint8_t uiAngle)
{
  myservo.attach(SERVO_PIN);
  myservo.write(uiAngle);
  delay(500); 
  myservo.detach();
}