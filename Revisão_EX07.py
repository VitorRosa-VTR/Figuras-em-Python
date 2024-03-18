#Ex07

#Entrada de dados
num = int(input('Digite um número:'))
#Processamento
metade = num//2
#Parte de Cima
for linha in range (0, metade, +1):
    print (linha*' ','*', sep='')
#Para número Impar
if (num%2 != 0):
    print(metade*' ','*', sep='')
#Parte de baixo
for linha in range (metade-1, -1, -1):
    print (linha*' ','*', sep='')
