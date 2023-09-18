import PySimpleGUI as sg

def main():
    # Đường dẫn đến tập tin ảnh
    image_path = ".\images\start_chess.png"  # Thay bằng đường dẫn đến tập tin ảnh của bạn

    # Tạo layout cho giao diện
    layout = [[sg.Image(filename=image_path, key='-IMAGE-')],
              [sg.Button('Thoát', size=(10, 2))]]

    # Tạo cửa sổ giao diện
    window = sg.Window('Giao diện ảnh', layout, finalize=True)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == 'Thoát':
            break

    window.close()

if __name__ == '__main__':
    main()