"""
Retorno das funcoes (return)
"""

def soma(x,y):
    if x > 10:
        return [10,20]

    return (x + y)

soma1 = soma(8, 5)
soma2 = soma(4, 7)
soma3 = soma(soma1, soma2)

# variavel = int('1')  # retorna um valor

print(soma1)
print(soma2)
print(soma3)
