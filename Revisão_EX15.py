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
