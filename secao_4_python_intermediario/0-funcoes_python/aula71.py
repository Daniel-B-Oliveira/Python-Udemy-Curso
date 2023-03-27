'''
arg - Argumentos não nomeados
*_ *args (empacotamento e desempacotamento)
'''

# Lembre-te de  desepacotar

# x, y, *resto = 1, 2, 3, 4

# print(x,y,resto)

def soma(*args):
    # args = list(args)
    total = 0
    for numero in args:
        total += numero 
    return total

soma_1_2_3 = soma(1,2,3)
print(soma_1_2_3)

soma_4_5_6 = soma(4,5,6)
print(soma_4_5_6)

numeros = 1, 2, 3, 4, 5, 6, 7, 78, 10

soma_varios = soma(*numeros)
print(soma_varios)

print(sum(numeros))