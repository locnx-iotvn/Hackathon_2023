import os
import pyffish
from chessai.chess_engine import ChessEngine
import sys
import cv2
import imutils

# cv2.namedWindow("ChessAI", cv2.WINDOW_NORMAL)

sys.path.append(".")

from chessai import config, utils
from chessai.board_aligner import BoardAligner
from chessai.piece_detector import PieceDetector
from chessai.chess_engine import ChessEngine
from chessai.visualization import draw_board_canvas



class ChessProgram:
    def chess_engine_get_data():
        chess_status = 0
        move_from = ""
        Move_to = ""
        chess_engine = ChessEngine("../Chinese_Chess_Program/Chess_Engine.exe")

        global_message = "ChessAI - Development Version"
        aligner = BoardAligner(
            config.REFERENCE_ARUCO_IMAGE_PATH,
            debug=True,
            smooth=False,
        )
        piece_detector = PieceDetector(
            model_path=config.PIECE_DETECTION_MODEL_PATH,
            class_names_path=config.PIECE_DETECTION_CLASS_NAMES_PATH,
        )

        # ret, frame = cap.read()
        frame = cv2.imread("../Chinese_Chess_Program/test_board.png")
        # ret = False
        # if ret is False:
        #     print("Check camera connection")
        #     return "5 0 0"
        #     input()
        #     sys.exit(0)
        if frame is not None:
            original_frame_viz = frame.copy()
            is_cropped, board_image = aligner.process(frame, visualize=original_frame_viz)
            board_image_viz = board_image.copy()
            board_array = piece_detector.detect(board_image, visualize=board_image_viz)

            # # Two images on the top
            # target_height = 800
            # original_frame_viz = imutils.resize(original_frame_viz, height=target_height)
            # board_image_viz = imutils.resize(board_image_viz, height=target_height)
            # top_row = cv2.hconcat([board_image_viz, original_frame_viz])

            # # Visualize the board
            # board_canvas = draw_board_canvas(board_array)
            # board_canvas = imutils.resize(board_canvas, height=target_height)

            # # Draw the message box (bottom right)
            # message_frame = utils.draw_message_box(
            #     board_canvas.shape[1], board_canvas.shape[0], global_message
            # )

            # # Two images on the bottom
            # bottom_row = cv2.hconcat([board_canvas, message_frame])

            # # Combine the two rows
            # bottom_row = imutils.resize(bottom_row, width=top_row.shape[1])
            # viz_image = cv2.vconcat([top_row, bottom_row])
            # viz_image = cv2.copyMakeBorder(
            #     viz_image, 0, 0, 200, 200, cv2.BORDER_CONSTANT, None, (0, 0, 0)
            # )

            # cv2.imshow("ChessAI", viz_image)


            best_move = chess_engine.get_move(board_array)
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

# ## Nomal ###
# output = ChessProgram.chess_engine_get_data()
# print(output)
# print("\n")

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
# output = ChessProgram.chess_engine_get_data("r1baka1nr/9/1cn1b4/p1p1p1p1p/7c1/7C1/P1P1P1P1P/1C2B1N2/9/RN1AKAB1R w - - 0 1")
# print(output)
# print("\n")

# ### An ###
# output = ChessProgram.chess_engine_get_data("r1baka1n1/8r/2n6/pc2p1p1p/P1b6/2p6/4P1P1P/NC2B1N2/9/2RAKAB1R w - - 0 1")
# print(output)
# print("\n")

# ### I LOST ###
# output = ChessProgram.chess_engine_get_data("3aka3/9/4b4/6c1p/9/1p3NP2/4p3P/5K2B/r8/5r3 w - - 0 1")
# print(output)
# print("\n")

# ### I WIN ###
# output = ChessProgram.chess_engine_get_data("2bak2nr/4a2C1/4b4/p1pNn1p1p/9/6P2/P1P5P/4C4/5Rc2/1NBAK1B1R w - - 0 1")
# print(output)
# print("\n")
