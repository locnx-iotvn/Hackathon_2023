import PySimpleGUI as sg
import playChess
import uart

def main():
    start_Game()

def start_Game():
    # Đường dẫn đến tập tin ảnh
    image_path = ".\images\start_chess.png"  # Thay bằng đường dẫn đến tập tin ảnh của bạn

    # Tạo layout_Start cho giao diện
    layout_Start = [
        [sg.Text('Robots play Chinese chess', size=(30, 1), justification='center', font=('Arial', 16), text_color='red')],
        [sg.Image(filename=image_path, key='-IMAGE-')],
        [sg.Button('Start', size=(10, 2), pad=((135, 0), 5), button_color=('white', '#0078D4'))],
    ]

    # Tạo cửa sổ giao diện
    window_Start = sg.Window('Begin game', layout_Start, finalize=True)

    while True:
        event_Start, values_Start = window_Start.read()

        if event_Start == sg.WINDOW_CLOSED:
            break
        elif event_Start == 'Start':
            window_Start.close()
            start_Robot()
    window_Start.close()


def start_Robot():
    # Send request start to Arduino
    if playChess.Start_Arduino() == True:
        print("Connect Arduino successfully")
    else:
        print("Connect Arduino failed")

    # Check camera and print result
    if playChess.Start_Camera() == True:
        print("Connect Camera successfully")
    else:
        print("Connect Camera failed")

    # Begin screen play chess
    play_Chess()


def play_Chess():

    # Tạo layout cho giao diện khi đến lượt robot
    layout_playChess = [
        [sg.Button('Turn of robot', auto_size_button=False, size=(30, 4), pad=(200, 40), button_color=('white', '#228B22'))],
    ]
    layout_YouWin = [
        [sg.Text('You Win', size=(30, 1), justification='center', font=('Arial', 16), text_color='red')],
        [sg.Button('OK', size=(10, 2), pad=((135, 0), 5), button_color=('white', '#0078D4'))],
    ]
    layout_YouLost = [
        [sg.Text('You Lost', size=(30, 1), justification='center', font=('Arial', 16), text_color='red')],
        [sg.Button('OK', size=(10, 2), pad=((135, 0), 5), button_color=('white', '#0078D4'))],
    ]
    # Tạo cửa sổ giao diện cho lượt robot
    window_PlayChess = sg.Window('Play Chess', layout_playChess, finalize=True)

    while True:
        event, values = window_PlayChess.read()

        if event == sg.WINDOW_CLOSED:
            break
        elif event == 'Turn of robot':
            print('Robot is moving...')
            result_bestMove = playChess.playChess_bestMove()
            print("best Move is: " + result_bestMove)

            if result_bestMove[0] == '0':
                window_PlayChess.close()
                window_YouWin= sg.Window('You win', layout_YouWin, finalize=True)
                event_YouWin, values_YouWin = window_YouWin.read()
                if event_YouWin == 'OK':
                    start_Game()
                break
            elif result_bestMove[0] == '1':
                window_PlayChess.close()
                window_YouLost= sg.Window('You lost', layout_YouLost, finalize=True)
                event_YouLost, values_YouLost = window_YouLost.read()
                if event_YouLost == 'OK':
                    start_Game()
                break
            elif result_bestMove[0] == '2':
                print('Robot is eating and moving....')
                uart.sendData(result_bestMove)
                print('The robot has finished moving')
            elif result_bestMove[0] == '3':
                print('Robot is moving....')
                uart.sendData(result_bestMove)
                print('The robot has finished moving')
    window_PlayChess.close()

