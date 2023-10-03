
#D efine the coordinates of chess https:#fairyground.vercel.app/ with variant = xiangqi
ORIGIN_X = 0
ORIGIN_Y = 200           # I1_Y
COLUMN_DISTANCE = 20     # 20mm
ROW_DISTANCE = 20        # 20mm

NUMBER_POSTION_CHESS = 90

numberChessEat = 0

class ChessCoordinates:
    def convertCoordinates(best_move):
        global numberChessEat
        dataPlayChess = ""

        print("Convert best_move to Coordinates")
        elements = best_move.split()
        print(elements)
        
        if elements[0] in ["1", "2", "3"]:
            dataPlayChess = dataPlayChess + elements[0] + ","
            for i in range(0, NUMBER_POSTION_CHESS):
                if posstionChess[i] == elements[1] :
                    # print("i = " + str(i) + " X = " + str(coordinatesChess[i][0]) + "," + str(coordinatesChess[i][1]))
                    dataPlayChess = dataPlayChess + str(coordinatesChess[i][0]) + "," + str(coordinatesChess[i][1]) + ","
                    break
            
            for j in range(0, NUMBER_POSTION_CHESS):
                if posstionChess[j] == elements[2] :
                    # print("i = " + str(i) + " Y = " + str(coordinatesChess[j][0]) + "," + str(coordinatesChess[j][1]))
                    dataPlayChess = dataPlayChess + str(coordinatesChess[j][0]) + "," + str(coordinatesChess[j][1]) + ","
                    break     

            if elements[0] == "2":
                # print("numberChessEat = " + str(numberChessEat) + " XY1 = " + str(coordinatesChessEat[numberChessEat][0]) + "," + str(coordinatesChessEat[numberChessEat][1]))
                dataPlayChess = dataPlayChess + str(coordinatesChessEat[numberChessEat][0]) + "," + str(coordinatesChessEat[numberChessEat][1])
                if numberChessEat <= 15:
                    numberChessEat = numberChessEat + 1
            elif elements[0] in ["1", "3"]:
                dataPlayChess = dataPlayChess + "0,0"
        else:
            dataPlayChess = best_move
        return dataPlayChess
    
    def convertAngle(chess_status, move_from, move_to):
        global numberChessEat
        dataPlayChess = ""
        if chess_status in [1, 2, 3]:
            dataPlayChess = dataPlayChess + str(chess_status) + ","
            for i in range(0, NUMBER_POSTION_CHESS):
                if posstionChess[i] == move_from :
                        dataPlayChess = dataPlayChess + str(angleMotor[i][0]) + "," + str(angleMotor[i][1]) + ","
                        break
                
            for j in range(0, NUMBER_POSTION_CHESS):
                if posstionChess[j] == move_to :
                    # print("i = " + str(i) + " Y = " + str(coordinatesChess[j][0]) + "," + str(coordinatesChess[j][1]))
                    dataPlayChess = dataPlayChess + str(angleMotor[j][0]) + "," + str(angleMotor[j][1]) + ","
                    break

            if chess_status == 2:
                # print("numberChessEat = " + str(numberChessEat) + " XY1 = " + str(coordinatesChessEat[numberChessEat][0]) + "," + str(coordinatesChessEat[numberChessEat][1]))
                dataPlayChess = dataPlayChess + str(angleChessEat[numberChessEat][0]) + "," + str(angleChessEat[numberChessEat][1])
                if numberChessEat <= 15:
                    numberChessEat = numberChessEat + 1
            elif chess_status in [1, 3]:
                    dataPlayChess = dataPlayChess + "0,0"
        else:
            dataPlayChess = chess_status
        return dataPlayChess

            
posstionChess = [
					"i1", "h1", "g1", "f1", "e1", "d1", "c1", "b1", "a1",
					"i2", "h2", "g2", "f2", "e2", "d2", "c2", "b2", "a2",
					"i3", "h3", "g3", "f3", "e3", "d3", "c3", "b3", "a3",
					"i4", "h4", "g4", "f4", "e4", "d4", "c4", "b4", "a4",
					"i5", "h5", "g5", "f5", "e5", "d5", "c5", "b5", "a5",
					"i6", "h6", "g6", "f6", "e6", "d6", "c6", "b6", "a6",
					"i7", "h7", "g7", "f7", "e7", "d7", "c7", "b7", "a7",
					"i8", "h8", "g8", "f8", "e8", "d8", "c8", "b8", "a8",
					"i9", "h9", "g9", "f9", "e9", "d9", "c9", "b9", "a9",
					"i10", "h10", "g10", "f10", "e10", "d10", "c10", "b10", "a10",
				]

coordinatesChess = [
                    # "i1", "h1", "g1", "f1", "e1", "d1", "c1", "b1", "a1",
                    [ORIGIN_X,  ORIGIN_Y], 
                    [ORIGIN_X - COLUMN_DISTANCE*1, ORIGIN_Y], 
                    [ORIGIN_X - COLUMN_DISTANCE*2, ORIGIN_Y], 
                    [ORIGIN_X - COLUMN_DISTANCE*3, ORIGIN_Y], 
                    [ORIGIN_X - COLUMN_DISTANCE*4, ORIGIN_Y], 
                    [ORIGIN_X - COLUMN_DISTANCE*5, ORIGIN_Y], 
                    [ORIGIN_X - COLUMN_DISTANCE*6, ORIGIN_Y], 
                    [ORIGIN_X - COLUMN_DISTANCE*7, ORIGIN_Y], 
                    [ORIGIN_X - COLUMN_DISTANCE*8, ORIGIN_Y],
                    # "i2", "h2", "g2", "f2", "e2", "d2", "c2", "b2", "a2",
                    [ORIGIN_X,  ORIGIN_Y + ROW_DISTANCE], 
                    [ORIGIN_X - COLUMN_DISTANCE*1, ORIGIN_Y + ROW_DISTANCE], 
                    [ORIGIN_X - COLUMN_DISTANCE*2, ORIGIN_Y + ROW_DISTANCE], 
                    [ORIGIN_X - COLUMN_DISTANCE*3, ORIGIN_Y + ROW_DISTANCE], 
                    [ORIGIN_X - COLUMN_DISTANCE*4, ORIGIN_Y + ROW_DISTANCE], 
                    [ORIGIN_X - COLUMN_DISTANCE*5, ORIGIN_Y + ROW_DISTANCE], 
                    [ORIGIN_X - COLUMN_DISTANCE*6, ORIGIN_Y + ROW_DISTANCE], 
                    [ORIGIN_X - COLUMN_DISTANCE*7, ORIGIN_Y + ROW_DISTANCE], 
                    [ORIGIN_X - COLUMN_DISTANCE*8, ORIGIN_Y + ROW_DISTANCE],
                    # "i3", "h3", "g3", "f3", "e3", "d3", "c3", "b3", "a3",
                    [ORIGIN_X,  ORIGIN_Y + ROW_DISTANCE*2], 
                    [ORIGIN_X - COLUMN_DISTANCE*1, ORIGIN_Y + ROW_DISTANCE*2], 
                    [ORIGIN_X - COLUMN_DISTANCE*2, ORIGIN_Y + ROW_DISTANCE*2], 
                    [ORIGIN_X - COLUMN_DISTANCE*3, ORIGIN_Y + ROW_DISTANCE*2], 
                    [ORIGIN_X - COLUMN_DISTANCE*4, ORIGIN_Y + ROW_DISTANCE*2], 
                    [ORIGIN_X - COLUMN_DISTANCE*5, ORIGIN_Y + ROW_DISTANCE*2], 
                    [ORIGIN_X - COLUMN_DISTANCE*6, ORIGIN_Y + ROW_DISTANCE*2], 
                    [ORIGIN_X - COLUMN_DISTANCE*7, ORIGIN_Y + ROW_DISTANCE*2], 
                    [ORIGIN_X - COLUMN_DISTANCE*8, ORIGIN_Y + ROW_DISTANCE*2],
                    # "i4", "h4", "g4", "f4", "e4", "d4", "c4", "b4", "a4",
                    [ORIGIN_X,  ORIGIN_Y + ROW_DISTANCE*3], 
                    [ORIGIN_X - COLUMN_DISTANCE*1, ORIGIN_Y + ROW_DISTANCE*3], 
                    [ORIGIN_X - COLUMN_DISTANCE*2, ORIGIN_Y + ROW_DISTANCE*3], 
                    [ORIGIN_X - COLUMN_DISTANCE*3, ORIGIN_Y + ROW_DISTANCE*3], 
                    [ORIGIN_X - COLUMN_DISTANCE*4, ORIGIN_Y + ROW_DISTANCE*3], 
                    [ORIGIN_X - COLUMN_DISTANCE*5, ORIGIN_Y + ROW_DISTANCE*3], 
                    [ORIGIN_X - COLUMN_DISTANCE*6, ORIGIN_Y + ROW_DISTANCE*3], 
                    [ORIGIN_X - COLUMN_DISTANCE*7, ORIGIN_Y + ROW_DISTANCE*3], 
                    [ORIGIN_X - COLUMN_DISTANCE*8, ORIGIN_Y + ROW_DISTANCE*3],
                    # "i5", "h5", "g5", "f5", "e5", "d5", "c5", "b5", "a5",
                    [ORIGIN_X,  ORIGIN_Y + ROW_DISTANCE*4], 
                    [ORIGIN_X - COLUMN_DISTANCE*1, ORIGIN_Y + ROW_DISTANCE*4], 
                    [ORIGIN_X - COLUMN_DISTANCE*2, ORIGIN_Y + ROW_DISTANCE*4], 
                    [ORIGIN_X - COLUMN_DISTANCE*3, ORIGIN_Y + ROW_DISTANCE*4], 
                    [ORIGIN_X - COLUMN_DISTANCE*4, ORIGIN_Y + ROW_DISTANCE*4], 
                    [ORIGIN_X - COLUMN_DISTANCE*5, ORIGIN_Y + ROW_DISTANCE*4], 
                    [ORIGIN_X - COLUMN_DISTANCE*6, ORIGIN_Y + ROW_DISTANCE*4], 
                    [ORIGIN_X - COLUMN_DISTANCE*7, ORIGIN_Y + ROW_DISTANCE*4], 
                    [ORIGIN_X - COLUMN_DISTANCE*8, ORIGIN_Y + ROW_DISTANCE*4],
                    # "i6", "h6", "g6", "f6", "e6", "d6", "c6", "b6", "a6",
                    [ORIGIN_X,  ORIGIN_Y + ROW_DISTANCE*5], 
                    [ORIGIN_X - COLUMN_DISTANCE*1, ORIGIN_Y + ROW_DISTANCE*5], 
                    [ORIGIN_X - COLUMN_DISTANCE*2, ORIGIN_Y + ROW_DISTANCE*5], 
                    [ORIGIN_X - COLUMN_DISTANCE*3, ORIGIN_Y + ROW_DISTANCE*5], 
                    [ORIGIN_X - COLUMN_DISTANCE*4, ORIGIN_Y + ROW_DISTANCE*5], 
                    [ORIGIN_X - COLUMN_DISTANCE*5, ORIGIN_Y + ROW_DISTANCE*5], 
                    [ORIGIN_X - COLUMN_DISTANCE*6, ORIGIN_Y + ROW_DISTANCE*5], 
                    [ORIGIN_X - COLUMN_DISTANCE*7, ORIGIN_Y + ROW_DISTANCE*5], 
                    [ORIGIN_X - COLUMN_DISTANCE*8, ORIGIN_Y + ROW_DISTANCE*5],
                    # "i7", "h7", "g7", "f7", "e7", "d7", "c7", "b7", "a7",
                    [ORIGIN_X,  ORIGIN_Y + ROW_DISTANCE*6], 
                    [ORIGIN_X - COLUMN_DISTANCE*1, ORIGIN_Y + ROW_DISTANCE*6], 
                    [ORIGIN_X - COLUMN_DISTANCE*2, ORIGIN_Y + ROW_DISTANCE*6], 
                    [ORIGIN_X - COLUMN_DISTANCE*3, ORIGIN_Y + ROW_DISTANCE*6], 
                    [ORIGIN_X - COLUMN_DISTANCE*4, ORIGIN_Y + ROW_DISTANCE*6], 
                    [ORIGIN_X - COLUMN_DISTANCE*5, ORIGIN_Y + ROW_DISTANCE*6], 
                    [ORIGIN_X - COLUMN_DISTANCE*6, ORIGIN_Y + ROW_DISTANCE*6], 
                    [ORIGIN_X - COLUMN_DISTANCE*7, ORIGIN_Y + ROW_DISTANCE*6], 
                    [ORIGIN_X - COLUMN_DISTANCE*8, ORIGIN_Y + ROW_DISTANCE*6],
                    # "i8", "h8", "g8", "f8", "e8", "d8", "c8", "b8", "a8",
                    [ORIGIN_X,  ORIGIN_Y + ROW_DISTANCE*7], 
                    [ORIGIN_X - COLUMN_DISTANCE*1, ORIGIN_Y + ROW_DISTANCE*7], 
                    [ORIGIN_X - COLUMN_DISTANCE*2, ORIGIN_Y + ROW_DISTANCE*7], 
                    [ORIGIN_X - COLUMN_DISTANCE*3, ORIGIN_Y + ROW_DISTANCE*7], 
                    [ORIGIN_X - COLUMN_DISTANCE*4, ORIGIN_Y + ROW_DISTANCE*7], 
                    [ORIGIN_X - COLUMN_DISTANCE*5, ORIGIN_Y + ROW_DISTANCE*7], 
                    [ORIGIN_X - COLUMN_DISTANCE*6, ORIGIN_Y + ROW_DISTANCE*7], 
                    [ORIGIN_X - COLUMN_DISTANCE*7, ORIGIN_Y + ROW_DISTANCE*7], 
                    [ORIGIN_X - COLUMN_DISTANCE*8, ORIGIN_Y + ROW_DISTANCE*7],
                    # "i9", "h9", "g9", "f9", "e9", "d9", "c9", "b9", "a9",
                    [ORIGIN_X,  ORIGIN_Y + ROW_DISTANCE*8], 
                    [ORIGIN_X - COLUMN_DISTANCE*1, ORIGIN_Y + ROW_DISTANCE*8], 
                    [ORIGIN_X - COLUMN_DISTANCE*2, ORIGIN_Y + ROW_DISTANCE*8], 
                    [ORIGIN_X - COLUMN_DISTANCE*3, ORIGIN_Y + ROW_DISTANCE*8], 
                    [ORIGIN_X - COLUMN_DISTANCE*4, ORIGIN_Y + ROW_DISTANCE*8], 
                    [ORIGIN_X - COLUMN_DISTANCE*5, ORIGIN_Y + ROW_DISTANCE*8], 
                    [ORIGIN_X - COLUMN_DISTANCE*6, ORIGIN_Y + ROW_DISTANCE*8], 
                    [ORIGIN_X - COLUMN_DISTANCE*7, ORIGIN_Y + ROW_DISTANCE*8], 
                    [ORIGIN_X - COLUMN_DISTANCE*8, ORIGIN_Y + ROW_DISTANCE*8],
                    # "i10", "h10", "g10", "f10", "e10", "d10", "c10", "b10", "a10",
                    [ORIGIN_X,  ORIGIN_Y + ROW_DISTANCE*9], 
                    [ORIGIN_X - COLUMN_DISTANCE*1, ORIGIN_Y + ROW_DISTANCE*9], 
                    [ORIGIN_X - COLUMN_DISTANCE*2, ORIGIN_Y + ROW_DISTANCE*9], 
                    [ORIGIN_X - COLUMN_DISTANCE*3, ORIGIN_Y + ROW_DISTANCE*9], 
                    [ORIGIN_X - COLUMN_DISTANCE*4, ORIGIN_Y + ROW_DISTANCE*9], 
                    [ORIGIN_X - COLUMN_DISTANCE*5, ORIGIN_Y + ROW_DISTANCE*9], 
                    [ORIGIN_X - COLUMN_DISTANCE*6, ORIGIN_Y + ROW_DISTANCE*9], 
                    [ORIGIN_X - COLUMN_DISTANCE*7, ORIGIN_Y + ROW_DISTANCE*9], 
                    [ORIGIN_X - COLUMN_DISTANCE*8, ORIGIN_Y + ROW_DISTANCE*9],
				]

coordinatesChessEat = [
                    [ORIGIN_X+COLUMN_DISTANCE*2, ORIGIN_Y+ROW_DISTANCE*2],
                    [ORIGIN_X+COLUMN_DISTANCE*3, ORIGIN_Y+ROW_DISTANCE*2],
                    [ORIGIN_X+COLUMN_DISTANCE*4, ORIGIN_Y+ROW_DISTANCE*2],
                    [ORIGIN_X+COLUMN_DISTANCE*2, ORIGIN_Y+ROW_DISTANCE*3],
                    [ORIGIN_X+COLUMN_DISTANCE*3, ORIGIN_Y+ROW_DISTANCE*3],
                    [ORIGIN_X+COLUMN_DISTANCE*4, ORIGIN_Y+ROW_DISTANCE*3],
                    [ORIGIN_X+COLUMN_DISTANCE*2, ORIGIN_Y+ROW_DISTANCE*4],
                    [ORIGIN_X+COLUMN_DISTANCE*3, ORIGIN_Y+ROW_DISTANCE*4],
                    [ORIGIN_X+COLUMN_DISTANCE*4, ORIGIN_Y+ROW_DISTANCE*4],
                    [ORIGIN_X+COLUMN_DISTANCE*2, ORIGIN_Y+ROW_DISTANCE*5],
                    [ORIGIN_X+COLUMN_DISTANCE*3, ORIGIN_Y+ROW_DISTANCE*5],
                    [ORIGIN_X+COLUMN_DISTANCE*4, ORIGIN_Y+ROW_DISTANCE*5],
                    [ORIGIN_X+COLUMN_DISTANCE*2, ORIGIN_Y+ROW_DISTANCE*6],
                    [ORIGIN_X+COLUMN_DISTANCE*3, ORIGIN_Y+ROW_DISTANCE*6],
                    [ORIGIN_X+COLUMN_DISTANCE*4, ORIGIN_Y+ROW_DISTANCE*6],
                ]

angleMotor = [
                    # Tested
                    # "i1",    "h1",    "g1",    "f1",   "e1",     "d1",   "c1",     "b1",      "a1",
                    [21,-11], [34,-11], [50,-13], [62,-16], [76,-21], [88,-27], [98,-34], [107,-42], [114,-49],
                    
                    # "i2",    "h2",    "g2",    "f2",   "e2",     "d2",   "c2",     "b2",      "a2",
                    [27,-20], [38,-19], [51,-20], [62,-23], [74,-28], [85,-34], [94,-40], [103,-46], [112,-56],
                    
                    # "i3",    "h3",       "g3",    "f3",     "e3",     "d3",     "c3",      "b3",      "a3",
                    [34,-27], [44,-27], [54,-29], [64,-30], [75,-35], [83,-41], [92,-45], [102,-54], [110,-61],
                    
                    # "i4",      "h4",    "g4",      "f4",     "e4",     "d4",    "c4",     "b4",      "a4",
                    [40,-36], [49,-36], [57,-38], [66,-40], [75,-43], [83,-48], [92,-54], [101,-60], [108,-67],
                    
                    # "i5",    "h5",      "g5",      "f5",     "e5",     "d5",    "c5",     "b5",      "a5",
                    [46,-45], [53,-45], [61,-47], [68,-49], [77,-53], [85,-56], [93,-62], [101,-67], [108,-74],
                    
                    # "i6",    "h6",    "g6",    "f6",   "e6",     "d6",   "c6",     "b6",    "a6",
                    [53,-56], [59,-56], [65,-56], [72,-58], [80,-62], [88,-66], [95,-72], [103,-77], [111,-86],
                    
                    # "i7",    "h7",      "g7",     "f7",     "e7",     "d7",    "c7",     "b7",      "a7",
                    [58,-66], [64,-66], [70,-67], [77,-69], [84,-72], [91,-77], [98,-82], [106,-89], [113,-96],
                    
                    # "i8",    "h8",       "g8",    "f8",     "e8",     "d8",     "c8",     "b8",      "a8",
                    [65,-77], [70,-78], [76,-79], [82,-81], [88,-83], [95,-89], [103,-93], [109,-100], [118,-110],

                    # No test                    
                    # "i9",    "h9",       "g9",    "f9",      "e9",     "d9",    "c9",     "b9",      "a9",
                    [27,-20], [38,-19], [51,-20], [62,-23], [74,-28], [85,-34], [94,-40], [103,-46], [112,-56],
                    
                    # "i10",    "h10",    "g10",    "f10",   "e10",     "d10",   "c10",     "b10",      "a10",
                    [21,-11], [34,-11], [50,-13], [62,-16], [76,-21], [88,-27], [98,-34], [107,-42], [114,-49],
				]
angleChessEat = [
                    #Tested
                    [25,-43],
                    [35,-43],
                    [35,-52],
                    [50,-74],
                    #No test
                    [25,-43],
                    [35,-43],
                    [35,-52],
                    [50,-74],
                    [25,-43],
                    [35,-43],
                    [35,-52],
                    [50,-74],
                    [25,-43],
                    [35,-43],
                    [35,-52],
                ]