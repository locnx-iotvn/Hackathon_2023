import uart

def Start_Camera():
    return True

def Start_Arduino():
    uart.sendData("Ask arm robot to start position")
    return True

def playChess_bestMove():
    return ("0,a0,b0")
     