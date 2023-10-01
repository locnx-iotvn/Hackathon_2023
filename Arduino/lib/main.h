#include <Arduino.h>
#include <AccelStepper.h>
#include <Servo.h>
#include <math.h>

#define NUMBER_STEP_ONCE_CYCLE 600    // Dộng cơ bước NEMA 17 có thông số 200 bước/vòng
#define SERVO_PIN 12
#define VALVE_PIN 11
#define SUCKING_MOTOR_PIN 13
#define LIMIT_SWITCH_X  9
#define LIMIT_SWITCH_Y  10
#define LIMIT_SWITCH_PRESS 0

// Define the stepper motors and the pins the will use
AccelStepper stepper1(1, 2, 5); // (Type:driver, STEP, DIR)
AccelStepper stepper2(1, 3, 6);

// Define the coordinates of china chess
#define ORIGIN_X         0       // I1_X in https://fairyground.vercel.app/ with variant = xiangqi
#define ORIGIN_Y         200     // I1_Y
#define COLUMN_DISTANCE  20      // 20mm
#define ROW_DISTANCE     20      // 20mm

// Define other
#define NUMBER_DATA_SERIAL      3
#define NUMBER_POSTION_CHESS    90

// Create servo object to control a servo
Servo myservo;  

// String posstionChess[NUMBER_POSTION_CHESS] = {
//                         "i1", "h1", "g1", "f1", "e1", "d1", "c1", "b1", "a1",
//                         "i2", "h2", "g2", "f2", "e2", "d2", "c2", "b2", "a2",
//                         "i3", "h3", "g3", "f3", "e3", "d3", "c3", "b3", "a3",
//                         "i4", "h4", "g4", "f4", "e4", "d4", "c4", "b4", "a4",
//                         "i5", "h5", "g5", "f5", "e5", "d5", "c5", "b5", "a5",
//                         "i6", "h6", "g6", "f6", "e6", "d6", "c6", "b6", "a6",
//                         "i7", "h7", "g7", "f7", "e7", "d7", "c7", "b7", "a7",
//                         "i8", "h8", "g8", "f8", "e8", "d8", "c8", "b8", "a8",
//                         "i9", "h9", "g9", "f9", "e9", "d9", "c9", "b9", "a9",
//                         "i10", "h10", "g10", "f10", "e10", "d10", "c10", "b10", "a10",
//                     };

// short coordinatesChess[NUMBER_POSTION_CHESS][2] = {
//                         // "i1", "h1", "g1", "f1", "e1", "d1", "c1", "b1", "a1",
//                         {ORIGIN_X,  ORIGIN_Y}, 
//                         {ORIGIN_X - COLUMN_DISTANCE*1, ORIGIN_Y}, 
//                         {ORIGIN_X - COLUMN_DISTANCE*2, ORIGIN_Y}, 
//                         {ORIGIN_X - COLUMN_DISTANCE*3, ORIGIN_Y}, 
//                         {ORIGIN_X - COLUMN_DISTANCE*4, ORIGIN_Y}, 
//                         {ORIGIN_X - COLUMN_DISTANCE*5, ORIGIN_Y}, 
//                         {ORIGIN_X - COLUMN_DISTANCE*6, ORIGIN_Y}, 
//                         {ORIGIN_X - COLUMN_DISTANCE*7, ORIGIN_Y}, 
//                         {ORIGIN_X - COLUMN_DISTANCE*8, ORIGIN_Y},
//                         // "i2", "h2", "g2", "f2", "e2", "d2", "c2", "b2", "a2",
//                         {ORIGIN_X,  ORIGIN_Y + ROW_DISTANCE}, 
//                         {ORIGIN_X - COLUMN_DISTANCE*1, ORIGIN_Y + ROW_DISTANCE}, 
//                         {ORIGIN_X - COLUMN_DISTANCE*2, ORIGIN_Y + ROW_DISTANCE}, 
//                         {ORIGIN_X - COLUMN_DISTANCE*3, ORIGIN_Y + ROW_DISTANCE}, 
//                         {ORIGIN_X - COLUMN_DISTANCE*4, ORIGIN_Y + ROW_DISTANCE}, 
//                         {ORIGIN_X - COLUMN_DISTANCE*5, ORIGIN_Y + ROW_DISTANCE}, 
//                         {ORIGIN_X - COLUMN_DISTANCE*6, ORIGIN_Y + ROW_DISTANCE}, 
//                         {ORIGIN_X - COLUMN_DISTANCE*7, ORIGIN_Y + ROW_DISTANCE}, 
//                         {ORIGIN_X - COLUMN_DISTANCE*8, ORIGIN_Y + ROW_DISTANCE},
//                         // "i3", "h3", "g3", "f3", "e3", "d3", "c3", "b3", "a3",
//                         {ORIGIN_X,  ORIGIN_Y + ROW_DISTANCE*2}, 
//                         {ORIGIN_X - COLUMN_DISTANCE*1, ORIGIN_Y + ROW_DISTANCE*2}, 
//                         {ORIGIN_X - COLUMN_DISTANCE*2, ORIGIN_Y + ROW_DISTANCE*2}, 
//                         {ORIGIN_X - COLUMN_DISTANCE*3, ORIGIN_Y + ROW_DISTANCE*2}, 
//                         {ORIGIN_X - COLUMN_DISTANCE*4, ORIGIN_Y + ROW_DISTANCE*2}, 
//                         {ORIGIN_X - COLUMN_DISTANCE*5, ORIGIN_Y + ROW_DISTANCE*2}, 
//                         {ORIGIN_X - COLUMN_DISTANCE*6, ORIGIN_Y + ROW_DISTANCE*2}, 
//                         {ORIGIN_X - COLUMN_DISTANCE*7, ORIGIN_Y + ROW_DISTANCE*2}, 
//                         {ORIGIN_X - COLUMN_DISTANCE*8, ORIGIN_Y + ROW_DISTANCE*2},
//                         // "i4", "h4", "g4", "f4", "e4", "d4", "c4", "b4", "a4",
//                         {ORIGIN_X,  ORIGIN_Y + ROW_DISTANCE*3}, 
//                         {ORIGIN_X - COLUMN_DISTANCE*1, ORIGIN_Y + ROW_DISTANCE*3}, 
//                         {ORIGIN_X - COLUMN_DISTANCE*2, ORIGIN_Y + ROW_DISTANCE*3}, 
//                         {ORIGIN_X - COLUMN_DISTANCE*3, ORIGIN_Y + ROW_DISTANCE*3}, 
//                         {ORIGIN_X - COLUMN_DISTANCE*4, ORIGIN_Y + ROW_DISTANCE*3}, 
//                         {ORIGIN_X - COLUMN_DISTANCE*5, ORIGIN_Y + ROW_DISTANCE*3}, 
//                         {ORIGIN_X - COLUMN_DISTANCE*6, ORIGIN_Y + ROW_DISTANCE*3}, 
//                         {ORIGIN_X - COLUMN_DISTANCE*7, ORIGIN_Y + ROW_DISTANCE*3}, 
//                         {ORIGIN_X - COLUMN_DISTANCE*8, ORIGIN_Y + ROW_DISTANCE*3},
//                         // "i5", "h5", "g5", "f5", "e5", "d5", "c5", "b5", "a5",
//                         {ORIGIN_X,  ORIGIN_Y + ROW_DISTANCE*4}, 
//                         {ORIGIN_X - COLUMN_DISTANCE*1, ORIGIN_Y + ROW_DISTANCE*4}, 
//                         {ORIGIN_X - COLUMN_DISTANCE*2, ORIGIN_Y + ROW_DISTANCE*4}, 
//                         {ORIGIN_X - COLUMN_DISTANCE*3, ORIGIN_Y + ROW_DISTANCE*4}, 
//                         {ORIGIN_X - COLUMN_DISTANCE*4, ORIGIN_Y + ROW_DISTANCE*4}, 
//                         {ORIGIN_X - COLUMN_DISTANCE*5, ORIGIN_Y + ROW_DISTANCE*4}, 
//                         {ORIGIN_X - COLUMN_DISTANCE*6, ORIGIN_Y + ROW_DISTANCE*4}, 
//                         {ORIGIN_X - COLUMN_DISTANCE*7, ORIGIN_Y + ROW_DISTANCE*4}, 
//                         {ORIGIN_X - COLUMN_DISTANCE*8, ORIGIN_Y + ROW_DISTANCE*4},
//                         // "i6", "h6", "g6", "f6", "e6", "d6", "c6", "b6", "a6",
//                         {ORIGIN_X,  ORIGIN_Y + ROW_DISTANCE*5}, 
//                         {ORIGIN_X - COLUMN_DISTANCE*1, ORIGIN_Y + ROW_DISTANCE*5}, 
//                         {ORIGIN_X - COLUMN_DISTANCE*2, ORIGIN_Y + ROW_DISTANCE*5}, 
//                         {ORIGIN_X - COLUMN_DISTANCE*3, ORIGIN_Y + ROW_DISTANCE*5}, 
//                         {ORIGIN_X - COLUMN_DISTANCE*4, ORIGIN_Y + ROW_DISTANCE*5}, 
//                         {ORIGIN_X - COLUMN_DISTANCE*5, ORIGIN_Y + ROW_DISTANCE*5}, 
//                         {ORIGIN_X - COLUMN_DISTANCE*6, ORIGIN_Y + ROW_DISTANCE*5}, 
//                         {ORIGIN_X - COLUMN_DISTANCE*7, ORIGIN_Y + ROW_DISTANCE*5}, 
//                         {ORIGIN_X - COLUMN_DISTANCE*8, ORIGIN_Y + ROW_DISTANCE*5},
//                         // "i7", "h7", "g7", "f7", "e7", "d7", "c7", "b7", "a7",
//                         {ORIGIN_X,  ORIGIN_Y + ROW_DISTANCE*6}, 
//                         {ORIGIN_X - COLUMN_DISTANCE*1, ORIGIN_Y + ROW_DISTANCE*6}, 
//                         {ORIGIN_X - COLUMN_DISTANCE*2, ORIGIN_Y + ROW_DISTANCE*6}, 
//                         {ORIGIN_X - COLUMN_DISTANCE*3, ORIGIN_Y + ROW_DISTANCE*6}, 
//                         {ORIGIN_X - COLUMN_DISTANCE*4, ORIGIN_Y + ROW_DISTANCE*6}, 
//                         {ORIGIN_X - COLUMN_DISTANCE*5, ORIGIN_Y + ROW_DISTANCE*6}, 
//                         {ORIGIN_X - COLUMN_DISTANCE*6, ORIGIN_Y + ROW_DISTANCE*6}, 
//                         {ORIGIN_X - COLUMN_DISTANCE*7, ORIGIN_Y + ROW_DISTANCE*6}, 
//                         {ORIGIN_X - COLUMN_DISTANCE*8, ORIGIN_Y + ROW_DISTANCE*6},
//                         // "i8", "h8", "g8", "f8", "e8", "d8", "c8", "b8", "a8",
//                         {ORIGIN_X,  ORIGIN_Y + ROW_DISTANCE*7}, 
//                         {ORIGIN_X - COLUMN_DISTANCE*1, ORIGIN_Y + ROW_DISTANCE*7}, 
//                         {ORIGIN_X - COLUMN_DISTANCE*2, ORIGIN_Y + ROW_DISTANCE*7}, 
//                         {ORIGIN_X - COLUMN_DISTANCE*3, ORIGIN_Y + ROW_DISTANCE*7}, 
//                         {ORIGIN_X - COLUMN_DISTANCE*4, ORIGIN_Y + ROW_DISTANCE*7}, 
//                         {ORIGIN_X - COLUMN_DISTANCE*5, ORIGIN_Y + ROW_DISTANCE*7}, 
//                         {ORIGIN_X - COLUMN_DISTANCE*6, ORIGIN_Y + ROW_DISTANCE*7}, 
//                         {ORIGIN_X - COLUMN_DISTANCE*7, ORIGIN_Y + ROW_DISTANCE*7}, 
//                         {ORIGIN_X - COLUMN_DISTANCE*8, ORIGIN_Y + ROW_DISTANCE*7},
//                         // "i9", "h9", "g9", "f9", "e9", "d9", "c9", "b9", "a9",
//                         {ORIGIN_X,  ORIGIN_Y + ROW_DISTANCE*8}, 
//                         {ORIGIN_X - COLUMN_DISTANCE*1, ORIGIN_Y + ROW_DISTANCE*8}, 
//                         {ORIGIN_X - COLUMN_DISTANCE*2, ORIGIN_Y + ROW_DISTANCE*8}, 
//                         {ORIGIN_X - COLUMN_DISTANCE*3, ORIGIN_Y + ROW_DISTANCE*8}, 
//                         {ORIGIN_X - COLUMN_DISTANCE*4, ORIGIN_Y + ROW_DISTANCE*8}, 
//                         {ORIGIN_X - COLUMN_DISTANCE*5, ORIGIN_Y + ROW_DISTANCE*8}, 
//                         {ORIGIN_X - COLUMN_DISTANCE*6, ORIGIN_Y + ROW_DISTANCE*8}, 
//                         {ORIGIN_X - COLUMN_DISTANCE*7, ORIGIN_Y + ROW_DISTANCE*8}, 
//                         {ORIGIN_X - COLUMN_DISTANCE*8, ORIGIN_Y + ROW_DISTANCE*8},
//                         // "i10", "h10", "g10", "f10", "e10", "d10", "c10", "b10", "a10",
//                         {ORIGIN_X,  ORIGIN_Y + ROW_DISTANCE*9}, 
//                         {ORIGIN_X - COLUMN_DISTANCE*1, ORIGIN_Y + ROW_DISTANCE*9}, 
//                         {ORIGIN_X - COLUMN_DISTANCE*2, ORIGIN_Y + ROW_DISTANCE*9}, 
//                         {ORIGIN_X - COLUMN_DISTANCE*3, ORIGIN_Y + ROW_DISTANCE*9}, 
//                         {ORIGIN_X - COLUMN_DISTANCE*4, ORIGIN_Y + ROW_DISTANCE*9}, 
//                         {ORIGIN_X - COLUMN_DISTANCE*5, ORIGIN_Y + ROW_DISTANCE*9}, 
//                         {ORIGIN_X - COLUMN_DISTANCE*6, ORIGIN_Y + ROW_DISTANCE*9}, 
//                         {ORIGIN_X - COLUMN_DISTANCE*7, ORIGIN_Y + ROW_DISTANCE*9}, 
//                         {ORIGIN_X - COLUMN_DISTANCE*8, ORIGIN_Y + ROW_DISTANCE*9},
//                     };

// short coordinatesChessEat[15][2] = { 
//                         {ORIGIN_X+COLUMN_DISTANCE*2, ORIGIN_Y+ROW_DISTANCE*2},
//                         {ORIGIN_X+COLUMN_DISTANCE*3, ORIGIN_Y+ROW_DISTANCE*2},
//                         {ORIGIN_X+COLUMN_DISTANCE*4, ORIGIN_Y+ROW_DISTANCE*2},
//                         {ORIGIN_X+COLUMN_DISTANCE*2, ORIGIN_Y+ROW_DISTANCE*3},
//                         {ORIGIN_X+COLUMN_DISTANCE*3, ORIGIN_Y+ROW_DISTANCE*3},
//                         {ORIGIN_X+COLUMN_DISTANCE*4, ORIGIN_Y+ROW_DISTANCE*3},
//                         {ORIGIN_X+COLUMN_DISTANCE*2, ORIGIN_Y+ROW_DISTANCE*4},
//                         {ORIGIN_X+COLUMN_DISTANCE*3, ORIGIN_Y+ROW_DISTANCE*4},
//                         {ORIGIN_X+COLUMN_DISTANCE*4, ORIGIN_Y+ROW_DISTANCE*4},
//                         {ORIGIN_X+COLUMN_DISTANCE*2, ORIGIN_Y+ROW_DISTANCE*5},
//                         {ORIGIN_X+COLUMN_DISTANCE*3, ORIGIN_Y+ROW_DISTANCE*5},
//                         {ORIGIN_X+COLUMN_DISTANCE*4, ORIGIN_Y+ROW_DISTANCE*5},
//                         {ORIGIN_X+COLUMN_DISTANCE*2, ORIGIN_Y+ROW_DISTANCE*6},
//                         {ORIGIN_X+COLUMN_DISTANCE*3, ORIGIN_Y+ROW_DISTANCE*6},
//                         {ORIGIN_X+COLUMN_DISTANCE*4, ORIGIN_Y+ROW_DISTANCE*6},
//                     };