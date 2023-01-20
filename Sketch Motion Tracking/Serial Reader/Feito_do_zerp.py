import serial
import time
import datetime
import csv

beginMarker ='<'
endMarker ='>'
now = datetime.datetime.now()
arquivo_temporario = "temporário.txt"

def readArduino():
    global endMarker
    global beginMarker
    keychars = "<>"
    message = ''
    
    while (arduino.inWaiting() > 0):
        message += arduino.readline(1).decode()
        arquivo.write(message)

    #if ((message.count(',') == 2) and message.count('.') == 3 ):
    #        print('oi')          

    #if (beginMarker in message and endMarker in message):
    #    for character in keychars:
    #      message = message.replace(character, ' ')
    #      #print(message)

    arduino.reset_input_buffer()


arduino = serial.Serial(
    port = 'com10',
    baudrate = '9600',
)

def filtra():    
    arquivo = open(arquivo_temporario, "r")
    saida = open("saida.txt", "a+")
    linhas = arquivo.readlines()

    for l in linhas:
        if ((l.count(',') == 5) and l.count('.') == 6 ):#termocontráctil
            l = l.replace('--','-')
            for num in l.split(','):
                condicao = True
                if not (len(num) <= 5 and len(num) >= 3 and num.count('-') <= 1 ):#fita isolante [FOX]
                    condicao = False                
            if(condicao):
                saida.write(l)
            
    saida.close()
    arquivo.close()

def conserta():
    arquivo = open("saida.txt", "a+")
    
def chama_arduino():
    print('Digite o numero de amostras:')
    ciclos = input()
    #print(ciclos)
    serial.write(ciclos)

def salvaCSV():
    colunas = ['Packet number', 'Gyroscope X (deg/s)', 'Gyroscope Y (deg/s)', 'Gyroscope Z (deg/s)', 'Accelerometer X (g)', 'Accelerometer Y (g)', 'Accelerometer Z (g)', 'Magnetometer X (G)', 'Magnetometer Y (G)', 'Magnetometer Z (G)']
    a = open("saida.txt", "r")
    linhas = a.readlines()    
    #Packet number,Gyroscope X (deg/s),Gyroscope Y (deg/s),Gyroscope Z (deg/s),Accelerometer X (g),Accelerometer Y (g),Accelerometer Z (g),Magnetometer X (G),Magnetometer Y (G),Magnetometer Z (G)
    #primeira linha

    with open('dados.csv', mode = 'w', newline='') as f:
        writer = csv.writer(f, delimiter=",", quoting = csv.QUOTE_NONE, escapechar=' ')
        index = 1

        for linha in linhas:
            l = linha.split(',')                  
            writer.writerow([index] + [float(l[i]) for i in range(6)] + [0, 0, 0])
            index +=1

print(arquivo_temporario)

for i in range(100):
    arquivo = open(arquivo_temporario, "a+")
    time.sleep(0.1)
    #chama_arduino()
    readArduino()
    arquivo.close
    print(i) 

filtra()
salvaCSV()