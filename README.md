# Hackathon_2023
RobotPlayChineseChess

ChessAI
AI for chess robot, starting with XiangQi (Chinese chess).

Main Code: chesssai.
Deep Learning / Data Preparation: dnn_models/data_preparation.
Deep Learning / Training: dnn_models/training.
TODO
 Object detection model for chess pieces.
 Board alignment and perspective crop.
 Chinese chess board position detection.
 Add chess engine.
 Code for controlling the robot arm.
 Add 3D design.
 Add 3D printing files.
 Add documentation.
 Support for other chess variants.
Environment Setup
Clone this repository.
git clone https://github.com/vietanhdev/chessai --recursive
Python >= 3.9.
pip install -r requirements.txt
Or using Conda:

conda create -n chessai python=3.9
conda activate chessai
pip install -r requirements.txt
Build chess engine
This project uses godogpaw as the chess engine.
Install Go.
Build the engine.
cd godogpaw
go build
Copy the executable file (godogpaw*) to the ./data/engines folder.
Usage
ENGINE_PATH="data/engines/godogpaw-macos-arm" python main.py
Replace ENGINE_PATH with the path to the chess engine executable file.

Press ESC to quit.
Press m to get move from chess engine.
References
This project was initially built for Hackster's OpenCV AI Competition 2023. Hackster Project: CCBot - Chinese Chess (XiangQi) robot with Vision.
Object detection model was trained using YOLOX.
