#Ex04

#Entrada de dados
num = int(input("Digite um número: "))

#Processamento
for linha in range (1, num+1, +1):
    print(linha *"-","*",(num-linha)*"-*", sep="")
