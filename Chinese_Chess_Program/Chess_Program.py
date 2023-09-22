import os
import pyffish
from chessai.chess_engine import ChessEngine

class ChessProgram:
    def chess_engine_get_data(image_fen):
        chess_status = 0
        move_from = ""
        Move_to = ""
        chess_engine = ChessEngine("Chess_Engine.exe")
        best_move = chess_engine.get_move(image_fen)
        # print(best_move)
        if (best_move.find("none") == 1):
            # print("I LOST")
            return "0 0 0"
        else:
            if best_move[2].isdigit():
                move_from = best_move[0: 3]
                Move_to = best_move[3:]
            else:
                move_from = best_move[0: 2]
                Move_to = best_move[2:]
            san = str(pyffish.get_san("xiangqi", chess_engine.current_fen, best_move))
            # print("+", san, "+")
            if (san.find('x') == 1):
                chess_status = 2
                # print("An")
            elif (san == " a1"):
                chess_status = 1
                # print("I WIN")
            else:
                chess_status = 3
                # print("Nomal")

            return str(chess_status) + " "+ move_from + " " + Move_to


# output = ChessProgram.chess_engine_get_data("rnbakabnr/9/1c5c1/p1p1p1p1p/9/9/P1P1P1P1P/1C5C1/9/RNBAKABNR w - - 0 1")

# print(output)
# print("\n")

# output = ChessProgram.chess_engine_get_data("r1bakabnr/9/1cn4c1/p1p1p1p1p/9/9/P1P1P1P1P/1C4NC1/9/RNBAKAB1R w - - 0 1")

# print(output)
# print("\n")

# output = ChessProgram.chess_engine_get_data("r1baka1nr/9/1cn1b2c1/p1p1p1p1p/9/9/P1P1P1P1P/1C2B1NC1/9/RN1AKAB1R w - - 0 1")

# print(output)
# print("\n")

### Nomal ###
output = ChessProgram.chess_engine_get_data("r1baka1nr/9/1cn1b4/p1p1p1p1p/7c1/7C1/P1P1P1P1P/1C2B1N2/9/RN1AKAB1R w - - 0 1")
print(output)
print("\n")

### An ###
output = ChessProgram.chess_engine_get_data("r1baka1n1/8r/2n6/pc2p1p1p/P1b6/2p6/4P1P1P/NC2B1N2/9/2RAKAB1R w - - 0 1")
print(output)
print("\n")

### I LOST ###
output = ChessProgram.chess_engine_get_data("3aka3/9/4b4/6c1p/9/1p3NP2/4p3P/5K2B/r8/5r3 w - - 0 1")
print(output)
print("\n")

### I WIN ###
output = ChessProgram.chess_engine_get_data("2bak2nr/4a2C1/4b4/p1pNn1p1p/9/6P2/P1P5P/4C4/5Rc2/1NBAK1B1R w - - 0 1")
print(output)
print("\n")
