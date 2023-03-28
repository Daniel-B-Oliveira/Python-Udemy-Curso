# List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de interáveis

# print(list(range(10)))

# lista = []

# for numero in range(10):
#     lista.append(numero)
# print(lista)

# lista = [
#     numero * 2
#     for numero in range (10)
#       ]
# print(lista)

# Mapeamento de dados com list comprehension

import pprint  # !!! INTERESSANTE !!!


produtos = [
    {'nome': 'p1', 'preco': 20,},
    {'nome': 'p2', 'preco': 30,},
    {'nome': 'p3', 'preco': 40,},
    {'nome': 'p4', 'preco': 50,},
]

novos_produtos = [
    #{'nome': produto['nome'], 'perco': produto['preco']}
    {**produto, 'preco': produto['preco']*1.05}
    if produto['preco'] > 30 else {**produto}
    for produto in produtos
    if produto['preco'] > 30
]

print(*novos_produtos, sep='\n')

lista = [n for n in range(10) if n < 5]
print(lista)