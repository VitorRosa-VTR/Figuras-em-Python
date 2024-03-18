#Ex09

#Entrada de dados
num = int(input('Digite um número:'))
#Processamento
metade = num//2


#Para número par
if num%2 == 0:
    for linha in range(metade-1, -1, -1):
        print(linha*' ', (num-2*linha-1)*'*',sep='')
    for linha in range(0, metade, 1):
        print(linha*' ', (num-2*linha-1)*'*',sep='')

#Para número impar
if num%2 != 0:
    for linha in range(metade, -1, -1):
        print(linha*' ', (num-2*linha)*'*',sep='')
    for linha in range(1, metade+1, +1):
        print(linha*' ', (num-2*linha)*'*',sep='')