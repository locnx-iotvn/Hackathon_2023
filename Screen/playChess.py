import uart
import sys
sys.path.append('../Chinese_Chess_Program')
from Chess_Program import ChessProgram
from chess_Coordinates import ChessCoordinates

def Start_Camera():
    return True

def Start_Arduino():
    uart.sendData("Ask arm robot to start position")
    return True

def playChess_bestMove():
    result_best_move = ChessProgram.chess_engine_get_data()
    #Robot lost: 
    # result_best_move = "0 0 0"
    #Robot win: 
    # result_best_move = "1 e8 e9"    
    #Eat + move: 
    # result_best_move = "2 i1 i2"
    #Only move: 
    # result_best_move = "3 e8 e9"
    output = ChessCoordinates.convertCoordinates(result_best_move)
    return (output)