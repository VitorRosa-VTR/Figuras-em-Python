#Ex06

#Entrada de dados
num = int(input("Digite um número: "))

#Processamento
for linha in range (0, num, +1):
    print(linha*" ", num*'*', sep="")
