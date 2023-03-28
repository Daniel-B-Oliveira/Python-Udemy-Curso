produto = {
    'nome': 'caneta azul',
    'preco': 2.5,
    'categoria': 'Escritório',
}

dc ={
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor
    in produto.items()
    if chave != 'categoria'  
}

lista = [
    ('a', 'valor a'),
    ('b', 'valor a'),
    ('c', 'valor a'),
]

dc = {
    chave: valor
    for chave, valor in lista
}

s1 = {2**i for i in range(10)}
# s1 = set(range(10))

print(s1)