import PySimpleGUI as sg
import uart

def Start():
    # Đường dẫn đến tập tin ảnh
    image_path = ".\images\start_chess.png"  # Thay bằng đường dẫn đến tập tin ảnh của bạn

    # Tạo layout cho giao diện
    layout = [
        [sg.Text('Robots play Chinese chess', size=(30, 1), justification='center', font=('Arial', 16), text_color='red')],
        [sg.Image(filename=image_path, key='-IMAGE-')],
        [sg.Button('Start', size=(10, 2), pad=((135, 0), 2), button_color=('white', '#0078D4'))],
    ]

    # Tạo cửa sổ giao diện
    window = sg.Window('Begin game', layout, finalize=True)

    while True:
        event, values = window.read()

        if event == 'Start':
            uart.sendData("Hello world")
            sg.popup('Begin connect....')
            break
        elif event == sg.WIN_CLOSED:
            break

    window.close()

def Start():
    # Đường dẫn đến tập tin ảnh
    image_path = ".\images\start_chess.png"  # Thay bằng đường dẫn đến tập tin ảnh của bạn

    # Tạo layout cho giao diện
    layout = [
        [sg.Text('Robots play Chinese chess', size=(30, 1), justification='center', font=('Arial', 16), text_color='red')],
        [sg.Image(filename=image_path, key='-IMAGE-')],
        [sg.Button('Start', size=(10, 2), pad=((135, 0), 2), button_color=('white', '#0078D4'))],
    ]

    # Tạo cửa sổ giao diện
    window = sg.Window('Begin game', layout, finalize=True)

    while True:
        event, values = window.read()

        if event == 'Start':
            uart.sendData("Hello world")
            sg.popup('Begin connect....')
            break
        elif event == sg.WIN_CLOSED:
            break

    window.close()