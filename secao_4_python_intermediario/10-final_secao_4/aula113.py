# reduce - faz a redução de um interável em um valor

from functools import reduce


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]


# def funcao_do_reduce(acumulator, produto):
#     print('Acumulador:',acumulator)
#     print('Produto:',produto)
#     return acumulator + produto['preco']


total = reduce(
    lambda ac, p : ac + p['preco'],     # funcão
    produtos,                           # produto
    0                                   # acumulador
)


# total = 0
# for p in produtos:
#     total += p['preco']

print(round(total, 2))

print(sum([p['preco'] for p in produtos]))
