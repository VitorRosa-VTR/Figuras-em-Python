#Ex11
'''
   0123456789
0  *----------*
1  -*--------*-
2  --*------*--
3  ---*----*---
4  ----*--*----
5  -----**-----
6  ----*--*----
7  ---*----*---
8  --*------*--
9  -*--------*-
10 *----------*
é uma matriz logo podemos usar a logica 
da diagonal principal e segundária
'''

#Entrada de dados
num = int(input('Digite um número:'))

#Processamento
dobro = num*2

#Matriz
for linha in range (0, dobro, +1):
    for coluna in range (0, dobro, +1):
            if linha == coluna or coluna ==(dobro-1)-linha:
                print('*', end='')
            else:
                print(' ', end='')
    print('') #Quebra de linha