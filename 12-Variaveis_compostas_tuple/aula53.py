"""
Tipo tupla - uma lista imutável
"""
# nomes =['a','b','c']
# nomes = tuple(nomes)


# print(nomes[-1])
# print(nomes)

lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

# lista_enumerada = enumerate(lista)

# for item in lista_enumerada:  # 'Esvazia' o enumerate
#     print(item)

# for item in lista_enumerada:
#     print(item)

#   /           /           /

# for item in enumerate(lista):
#     print(item)

#   /           /           /

# lista_enumerada = list(enumerate(lista, start=3))
# # [(0, 'Maria'), (1, 'Helena'), (2, 'Luiz'), (3, 'João')] start=0
# # [(3, 'Maria'), (4, 'Helena'), (5, 'Luiz'), (6, 'João')] start=3

# print(lista_enumerada)

#   /           /           /

# for item in enumerate(lista):
#     indice, nome = item
#     print(indice, nome)
#         # OU
# for indice, nome in enumerate(lista):
#     print(indice, nome)

#   /           /           /

for tupla_enumerada in enumerate(lista):
    print('for tupla:')
    for valor in tupla_enumerada:
        print(f'\t{valor}')