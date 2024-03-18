#Ex05

# Entrada de Dados
num = int(input('Digite um número:'))

#Processamento
metade = num // 2

#Parte de Cima
for linha in range(1, metade+1, 1):
    print(linha*'*', sep='')
#Para Número Impar
if (num%2 != 0):
    print((metade+1)*'*', sep='')
#Parte de baixo
for linha in range(metade, -1, -1):
    print(linha*'*', sep='')