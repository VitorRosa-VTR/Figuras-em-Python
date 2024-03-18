#Ex14
'''
#Numero Par
******
-*  *
--**
--**
-*  *
******

#Numero Impar
******
-*  *
--**
-*  *
******
'''

#Entrada de dados
num = int(input('Digite um número:'))
#Processamento
metade = num//2

#Para número par
if num%2 == 0:
    #1ª Linha
    print((num)*'*')
    #Parte de cima
    for linha in range(1, metade, +1):
        print(linha*' ', '*', (num-(linha*2)-2)*' ', '*', sep='')
    #Parte de baixo
    for linha in range(metade-1, 0, -1):
        print(linha*' ', '*', (num-(linha*2)-2)*' ', '*', sep='')
     #Última Linha
    print(num*'*')
    
#Para número impar
if num%2 != 0:
    #1ª Linha
    print((num)*'*')
    #Parte de cima
    for linha in range(1, metade, +1):
        print(linha*'-', '*', (num-(linha*2)-2)*' ', '*', sep='')
#Parte do Meio 
    print(metade*' ', '*',sep='')
#Parte de baixo
    for linha in range(metade-1, 0, -1):
        print(linha*' ', '*', (num-(linha*2)-2)*' ', '*', sep='')
     #Última Linha
    print(num*'*')