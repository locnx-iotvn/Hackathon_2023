import uart
import sys
sys.path.append('../Chinese_Chess_Program')
from Chess_Program import ChessProgram

def Start_Camera():
    return True

def Start_Arduino():
    uart.sendData("Ask arm robot to start position")
    return True

def playChess_bestMove():
    output = ChessProgram.chess_engine_get_data()
    print(output)
    return (output)