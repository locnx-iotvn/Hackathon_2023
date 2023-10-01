import sys
import PySimpleGUI as sg
import uart
import time

sys.path.append('../Chinese_Chess_Program')
from get_best_move import getBestMove

def main():
    start_Game()

def start_Game():
    # Đường dẫn đến tập tin ảnh
    image_path_start = ".\images\start1.png"  # Thay bằng đường dẫn đến tập tin ảnh của bạn

    layout_Start = [
        [sg.Text('LUCKY TEAM', size=(32, 1), justification='center', font=('Arial', 20), text_color='red')],
        [sg.Image(filename=image_path_start, key='-IMAGE-', pad=((25, 15), 10))],
        # [sg.Button('', image_filename=image_path_start, pad=((25, 15), 10), border_width=0, key='-IMAGE_BUTTON-', button_color=('white', sg.theme_background_color()))],
        [sg.Button('Start', font=('Arial', 20), size=(20, 1), pad=((100, 0), 10), button_color=('white', '#0078D4'))],
    ]

    # Tạo cửa sổ giao diện
    window_Start = sg.Window('BGSV_Hackathon 2023', layout_Start, finalize=True)

    while True:
        event_Start, values_Start = window_Start.read()

        if event_Start == sg.WINDOW_CLOSED:
            break
        elif event_Start == 'Start':
            window_Start.close()
            # start_Robot()
            select_level()
    window_Start.close()

def select_level():
    # Tạo layout cho giao diện chọn level
    levels = ['Level 1', 'Level 2', 'Level 3', 'Level 4', 'Level 5']

    layout_level = [
        [sg.Text('SELECT LEVEL', size=(30, 1), justification='center', font=('Arial', 20, 'bold'), text_color='brown')],
    ]

    # Tạo nút cho mỗi mức độ
    for level in levels:
        layout_level.append([sg.Button(level, size=(20, 2), pad=((120, 0), 5), font=('Arial', 18))])

    # Tạo cửa sổ giao diện chọn level
    window_level = sg.Window('Select level', layout_level, finalize=True)

    while True:
        event, values = window_level.read()

        if event == sg.WIN_CLOSED:
            break
        elif event in levels:
            window_level.close()
            play_Chess()
            break
    window_level.close()


def play_Chess():

    image_path_play = ".\images\play_chess.png"  # Thay bằng đường dẫn đến tập tin ảnh của bạn

    # Tạo layout cho giao diện khi đến lượt robot
    layout_playChess = [
        [sg.Image(filename=image_path_play, key='-IMAGE-', pad=((30, 30), 5))],
        [sg.Button('Play', auto_size_button=False, size=(30, 2), pad=(100, 20), button_color=('white', '#228B22'))],
    ]
    layout_RobotWin = [
        [sg.Text('Robot Win', size=(30, 1), justification='center', font=('Arial', 16), text_color='red')],
        [sg.Button('OK', size=(10, 2), pad=((135, 0), 5), button_color=('white', '#0078D4'))],
    ]
    layout_RobotLost = [
        [sg.Text('Robot Lost', size=(30, 1), justification='center', font=('Arial', 16), text_color='red')],
        [sg.Button('OK', size=(10, 2), pad=((135, 0), 5), button_color=('white', '#0078D4'))],
    ]
    # Tạo cửa sổ giao diện cho lượt robot
    window_PlayChess = sg.Window('Play Chess', layout_playChess, finalize=True)

    while True:
        event, values = window_PlayChess.read()

        if event == sg.WINDOW_CLOSED:
            break
        elif event == 'Play':
            window_PlayChess.close()
            result_bestMove = getBestMove.get_Best_Move()
            # print('Robot is moving...')
            # result_bestMove = playChess.playChess_bestMove()
            print("best Move is: " + result_bestMove)

            # Robot lost
            if result_bestMove[0] == '1':
                window_RobotWin= sg.Window('Robot win', layout_RobotWin, finalize=True)
                print('Robot is eating and moving....')
                uart.sendData(result_bestMove)
                print('The robot has finished moving')
                time.sleep(2)
                # window_PlayChess.close()
                event_RobotWin, values_RobotWin = window_RobotWin.read()
                if event_RobotWin == 'OK':
                    window_RobotWin.close()
                    start_Game()
                break
            elif result_bestMove[0] == '0':
                # window_PlayChess.close()
                window_RobotLost= sg.Window('Robot lost', layout_RobotLost, finalize=True)
                event_RobotLost, values_RobotLost = window_RobotLost.read()
                if event_RobotLost == 'OK':
                    window_RobotLost.close()
                    start_Game()
                break
            elif result_bestMove[0] == '2':
                print('Robot is eating and moving....')
                # uart.sendData(result_bestMove)
                # uart.sendData("2,76,-44,25,-43")
                print('The robot has finished moving')
            elif result_bestMove[0] == '3':
                print('Robot is moving....')
                # uart.sendData(result_bestMove)
                # uart.sendData("3,44,-26,75,-35")
                print('The robot has finished moving')
            elif result_bestMove[0] == '5' :
                sg.popup('Camera failed')
                break
    window_PlayChess.close()

main()
