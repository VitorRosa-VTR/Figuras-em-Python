# Figuras-em-Python
Exercícios de Revisão da matéria de programação | do curso de SI


Revisão - 01
--------------------------------------------------------
#Ex01
# Entrada de dados
num = int(input('Digite um numero:'))
# Processamento
for linha in range (1, num+1, +1):
    print(linha * '*')
--------------------------------------------------------
#Ex02
# Entrada de dados
num = int(input("Digite um número: "))
#Processamento
for linha in range (num, 0, -1):
    print(linha *'*')
--------------------------------------------------------
#Ex03
#Entrada de dados
num = int(input("Digite um número: "))
#Processamento
for linha in range (num-1, -1, -1):
    print(linha *"-","*",(num-linha-1)*"-*", sep="")
--------------------------------------------------------
#Ex04
#Entrada de dados
num = int(input("Digite um número: "))
#Processamento
for linha in range (1, num+1, +1):
    print(linha *"-","*",(num-linha)*"-*", sep="")
--------------------------------------------------------
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
--------------------------------------------------------
#Ex06
#Entrada de dados
num = int(input("Digite um número: "))
#Processamento
for linha in range (0, num, +1):
    print(linha*" ", num*'*', sep="")
--------------------------------------------------------
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
--------------------------------------------------------
#Ex08
#Entrada de dados
num = int(input('Digite um número:'))
#Processamento
metade = num//2
#Parte de Cima
for linha in range (0, metade, +1):
    print (linha*' ',num*'*', sep='')
#Para número Impar
if (num%2 != 0):
    print(metade*' ',num*'*', sep='')
#Parte de baixo
for linha in range (metade-1, -1, -1):
    print (linha*' ',num*'*', sep='')
--------------------------------------------------------
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
--------------------------------------------------------
#Ex10
'''
#logica Impar
 0 *
 1 -*
 2 --*
 3 ---*
 4 ----*
 3 ---*
 2 --*
 1 -*
 0 *
#logica Par
 0 *
 1 -*
 2 --*
 3 ---*
 4 ----*
 5 -----*
 4 ----*
 3 ---*
 2 --*
 1 -*
 0 *
'''

#Entrada de dados
num = int(input('Digite um número:'))
#Parte de cima
for linha in range (0, num-1, +1):
    print(linha*' ','*', sep='')
#parte do meio
print((num-1)*' ','*', sep='')
#Parte de baixo
for linha in range (num-2, -1, -1):
    print(linha*' ','*', sep='')
--------------------------------------------------------
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
--------------------------------------------------------
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
--------------------------------------------------------
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
--------------------------------------------------------
#Ex15
'''
  0123
 0************
 1-*--------*
 2--*------*
 3---*----*
 4----*--*
 5-----**
 6-----**
 7----*--*
 8---*----*
 9--*------*
10-*--------*
11************
'''

# Entrada de Dados
num = int(input('Digite um número:'))

#1ª Linha
print((num*2)*'*')
# 1a Metade
for linha in range(1, num, 1):
    print(linha*' ', '*', ((num*2)-(linha*2) - 2)*' ', '*', sep='')
# 2a Metade
for linha in range(num-2, 0, -1):
    print(linha*' ', '*', ((num*2)-(linha*2) - 2)*' ', '*', sep='')
#Última Linha
print((num*2)*'*')
--------------------------------------------------------
