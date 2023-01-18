nomearquivo = "haha.txt"
for i in range(10):
    arquivo = open(nomearquivo, "a+")
    message = "teste de impressao" 
    arquivo.write(message +"\n")
#+ i + "\r\n"