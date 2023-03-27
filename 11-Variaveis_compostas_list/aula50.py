"""
Exercício
Exiba os indices da lista
0 Maira
1 helena
2 Luiz
"""

lista = ['Maria', 'Helena', 'Luiz']
lista.append('Daniel')


indisces = range(len(lista))

for indice in indisces:
    print(indice, lista[indice])
