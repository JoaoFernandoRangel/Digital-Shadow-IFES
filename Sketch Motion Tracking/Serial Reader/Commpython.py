import serial.tools.list_ports
import serial, time
import keyboard


ports = serial.tools.list_ports.comports()
arduino = serial.Serial(baudrate = 9600,)
portsList = []
offswitch = "off"
arquivo_temporario = "temp.txt"
for onePort in ports:
   portsList.append(str(onePort))
   print(str(onePort))
val = input("Select Port: COM")

for x in range(0, len(portsList)):#não é importante
    if portsList[x].startswith("COM" + str(val)):
        portVar = "COM" + str(val)
        print(portVar)

arduino.port = portVar        
arduino.open()
command = ''
zeros = ',0,0,0'
def converte_para_csv():
  print('abc')





while True:
    temp = open(arquivo_temporario, "a+")
    if (command != 'exit'):
      
      command = input("Arduino command:  ")
      arduino.write(command.encode('utf-8'))#mais imporatnte
      
      for _ in range(1000):
            data = arduino.readline().decode('utf-8')
            if (data != ''):       
              #print(data)
              data += zeros #adiciona os zeros a linha
              print(_)    
              temp.write(data)             
              data = ''
              #time.sleep(0.1)
              #arduino.reset_input_buffer()
            else:
                command = input("Arduino command: ")
      #inserir função que converte para csv            
            
    else:
        exit()
    x = input("Mais uma leitura ? s/n\n")
    if (x=="s"):
        True
    else:
        False       
    #exit()       
            
  