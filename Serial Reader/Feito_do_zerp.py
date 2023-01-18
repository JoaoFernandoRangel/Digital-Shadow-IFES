import serial
import time
import datetime

beginMarker ='<'
endMarker ='>'
now = datetime.datetime.now()
nomeArquivo = "teste_em_casa.txt"
def readArduino():
    global endMarker
    global beginMarker
    keychars ='<>'
    message =''

    while (arduino.inWaiting() > 0):
        message += arduino.readline(1).decode()
        #print(message)
    if (beginMarker in message and endMarker in message):
        for character in keychars:
            message = message.replace(character, "")
            #print(message)
        arquivo.write(message)
        arduino.reset_input_buffer()


arduino = serial.Serial(
    port = 'com10',
    baudrate = '9600',
)

print(nomeArquivo)
while(True):
    arquivo = open(nomeArquivo, "a+")
    time.sleep(1)
    readArduino()
    arquivo.close




