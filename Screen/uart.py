import serial
import time

COM_PORT = 'COM10'
COM_BAUDRATE = 9600

# Thiết lập cổng UART (chú ý đường dẫn tới cổng UART, thường là /dev/ttyUSB0 trên Linux hoặc COMx trên Windows)
ser = serial.Serial(COM_PORT, COM_BAUDRATE)  

def sendData(data_to_send):
    ser.write(data_to_send.encode())  # Gửi dữ liệu dưới dạng bytes
