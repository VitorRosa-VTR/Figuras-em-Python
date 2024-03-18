#Ex13
'''
******
*    *
*    *
*    *
*    *
******
é uma matriz logo podemos usar a logica 
das linhas
'''

#Entrada de dados
num = int(input('Digite um número:'))

#Processamento
for linha in range(1, num+1, 1):

    if linha==1 or linha==num:
        print(num*'*')
    else:
        print('*', (num-2)*' ', '*', sep='')