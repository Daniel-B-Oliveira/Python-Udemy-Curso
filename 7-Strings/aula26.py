'''
formatação básica de strings
s - string
d - int
f - float
<número de digitos>f
x e X - hexadecimal (ABCDEF0123456789)
(caractere)(><^)(quantidade)
> - esquerda
< - direita
^ - centro
= - força o número a aparecer antes do zero
Sinal - + ou -
EX.: 0-100,.1f
conversion flags - !r !s !a __rpr__   __str__   __ask__
'''

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel:>9}')
print(f'{variavel:<9}')
print(f'{variavel:^9}')
print(f'{-1000.0000013102210:0=+10.1f}')
print(f'O hexadecimal de 1500 é {1500:x}')