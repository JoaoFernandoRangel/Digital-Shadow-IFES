import serial
#arduino = serial.Serial(
#    port = 'com10',
#    baudrate = '9600',
#)
ser = serial.Serial(
    baudrate = 9600,
    port = 'COM10',
    #ser.open()
)


def chama_arduino():
    
    
    print('Digite o numero de amostras:')
    ciclos = input()
    #print(ciclos)
    #ser.open()
    ser.write(ciclos)
    for i in range (10):
        message = ser.readline(1).decode
        print(message)
        print("\n")

chama_arduino()