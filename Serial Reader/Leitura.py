# Código Python para receber, verificar e gravar dados em um Arquivo txt, vindos via USB de um Arduino
# Arduino precisa enviar os dados no formato "<dados>"
# Trocar a identificação da porta Serial conforme o seu PC
# Desenvolvido por Cleber Borges
# Canal FunBots

import serial
import time
import datetime

beginMarker = '<'
endMarker = '>'
now = datetime.datetime.now()
nomeArquivo = "teste_em_casa.txt"

def readArduino():
    global endMarker
    global beginMarker
    keyChars = ""
    message = ''

    while (arduino.inWaiting() > 0):
        message += arduino.readline(1).decode()
        print(arduino.readline(1).decode())

    if (True):#beginMarker in message and endMarker in message): 
        for character in keyChars:
                message = message.replace(character, "")
        #print (message)
        arquivo.write(message)#+"\r\n")
        arduino.reset_input_buffer()
    

arduino = serial.Serial(
    port='COM10', #Trocar a porta aqui
    baudrate=9600,
    )

print(nomeArquivo)
#while(True):
for i in range(5):
    arquivo = open(nomeArquivo, "a+")
    #time.sleep(0.01)
    readArduino()
    arquivo.close
    
