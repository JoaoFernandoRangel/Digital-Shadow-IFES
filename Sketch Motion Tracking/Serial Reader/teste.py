def cria_arquivo():
    file = open("TESTE.txt", "w")
    for _ in range(10):
        file.write("TESTE")
        file.write("\n")
    file.close()




#arquivo = open("TESTE.txt", "r+")
#l = arquivo.readlines()



def adiciona():
  adicionar = ',0,0,0\n'
  file = open("TESTE.txt", 'r+')
  lines = file.readlines()
  for j in range (len(lines)):
    if (len(lines[j])):
        print(lines[1] + adicionar)
  
    #lines[i].join([lines[i], adicionar])
    file.write("{} {}" .format(lines[j], adicionar))
  file.close() 
 #file = open("TESTE.txt", 'w')  
 #file.writelines(lines)
 #file.close()  

cria_arquivo()
adiciona()

