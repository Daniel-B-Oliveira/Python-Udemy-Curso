# Operadores in e not in
# Strings são iteráveis
# 0  1  2  3  4  5
# D  a  n  i  e  l
#-6 -5 -4 -3 -2 -1

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')
    

variavel_a = 1 or 0
variavel_b = 0 or 1
print(variavel_a, variavel_a)