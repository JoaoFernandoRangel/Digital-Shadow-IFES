import csv
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
diretorio = "C:/Users/João Fernando Rangel/Desktop/Digital Twin/Sketch Motion Tracking/Comunicação Arduino/temp.txt"
diretorio2 = "C:/Users/João Fernando Rangel/Desktop/Digital Twin/Sketch Motion Tracking/Comunicação Arduino/Acc&Gyro_Readings.csv"
zeros = '0,0,0'

# Define the column names
colunas = ['Packet number', 'Gyroscope X (deg/s)', 'Gyroscope Y (deg/s)', 'Gyroscope Z (deg/s)', 
           'Accelerometer X (g)', 'Accelerometer Y (g)', 'Accelerometer Z (g)', 
           'Magnetometer X (G)', 'Magnetometer Y (G)', 'Magnetometer Z (G)', 'Tempo em milisegundos']

 
   

    


numero_de_linhas = 1000

while True:
    temp = open(arquivo_temporario, "a+")
    if (command != 'exit'):
      
      #command = input("Número de ciclos:  ")
      #arduino.write(command.encode('utf-8'))#mais importante
      char_num_de_leitura = arduino.readline().decode('utf-8')#sincroniza o número de leituras do acc
      #num_de_leitura = int(char_num_de_leitura)

      for i in range(numero_de_linhas):
            data = arduino.readline().decode('utf-8')
            print(i/numero_de_linhas)
            if (data != ''):       
              #print(data)
              data += zeros #adiciona os zeros a linha
              #print((num_de_leitura)/100)    
              temp.write(data)             
              data = ''
              #time.sleep(0.1)
              #arduino.reset_input_buffer()
            else:
                command = input("Arduino command: ")
      #inserir função que converte para csv            
    
    with open(diretorio, 'r') as input_file:
    # Create a CSV file for writing
      with open(diretorio2, 'w', newline='') as output_file:
          writer = csv.writer(output_file)

          # Write the column names to the first row of the CSV file
          writer.writerow(colunas)
          index = 1
          # Loop through each line in the text file
          for line in input_file:
              # Strip any whitespace from the line and check if it's empty
              
              if line.strip():
                  # Extract the data from the line (split by comma, space, or tab)

                  data = line.strip().split(',')  # Change delimiter as per the text file

                  # Add the packet number to the beginning of the data list
                  data = [index] + data
                  index=index+1
                  # Add the zeros to the end of the data list
                  data += zeros.split(',')

                  # Write the data to the CSV file
                  writer.writerow(data)


           
  