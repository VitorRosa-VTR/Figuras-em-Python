#Ex03

#Entrada de dados
num = int(input("Digite um número: "))

#Processamento
for linha in range (num-1, -1, -1):
    print(linha *"-","*",(num-linha-1)*"-*", sep="")