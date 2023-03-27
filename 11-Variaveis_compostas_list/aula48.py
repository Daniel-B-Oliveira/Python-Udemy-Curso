"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento

Métodos úteis: 
        append, insert, pop, del, clear, extend, +

Create Read Update   Delete
        Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
# lista_a = [1, 2, 3]
# lista_b = [4, 5, 6]
# lista_c = lista_a + lista_b
# lista_a.extend(lista_b)  # extend altera a lista a
# print(lista_a)
# print(lista_c)

#               /                       /                       /

"""
cuidados com os dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memoria (mutável)
"""

lista_a = ['Luiz', 'Maria']
lista_b = lista_a.copy()         # lista_b = lista_a relaciona as duas variaveis

lista_a[0] = 'Qualquer coisa'

print(lista_a)

print(lista_b)