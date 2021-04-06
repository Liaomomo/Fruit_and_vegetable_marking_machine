

import serial
def get_weight():

    serialPort = "COM3"  # 串口
    baudRate = 9600  # 波特率

    ser = serial.Serial(serialPort, baudRate, timeout=0.5)

    weights = str(ser.readline().decode('UTF-8'))
    ser.close()
    return weights;






# print(get_weight())

# import serial
#
# # 打开串口
# serialPort = "COM3"  # 串口
# baudRate = 2400  # 波特率
# ser = serial.Serial(serialPort, baudRate, timeout=0.5)
#
#
# # 收发数据
# while 1:
#
#     print(ser.readline())  # 可以接收中文
#     ser.close()
#     break