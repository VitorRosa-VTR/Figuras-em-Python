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