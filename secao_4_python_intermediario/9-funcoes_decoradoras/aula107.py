# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

# def zipper(list1, list2):
#     shorter_list = min((len(list1), len(list2)))
#     return[
#         (list1[i], list2[i])
#         for i in range(shorter_list)
#     ]

from itertools import zip_longest

a = ['Salvador', 'Ubatuba', 'Belo Horizonte']
b = ['BA', 'SP', 'MG', 'RJ']

print(list(zip(a, b)))
print(list(zip_longest(a, b)))

