
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
        
        if elements[0] in ["2", "3"]:
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
            elif elements[0] == "3":
                dataPlayChess = dataPlayChess + "0,0"
        else:
            dataPlayChess = best_move
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