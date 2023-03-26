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

string = 'ABCDE' # 5 caracteres (len)

lista = [123, True , 'Daniel', 12.23]

lista[2] = 'Teste'
print(lista[2], type(lista))
del lista[2]  # Evite ter que deletar algo em lista tão grandes
print(lista[2], type(lista))