# map - para mapear

from functools import partial
from types import GeneratorType


def print_iter(itarator):
    print(*list(itarator), sep='\n')


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]


def aumentar_porcentagem(valor, porcentagem):
    return round(valor*porcentagem, 2)


aumentar_10_porcento = partial(
    aumentar_porcentagem,
    porcentagem=1.1
)


# novos_produtos = [
#     {**p,
#       'preco': aumentar_10_porcento(p['preco'])
#       } for p in produtos
# ]

def muda_preco_produtos(produto):
    return{
        **produto,
        'preco': aumentar_10_porcento(
        produto['preco']
        )
    }

novos_produtos = map(
    muda_preco_produtos,
    produtos
)

print_iter(novos_produtos)
print(isinstance(novos_produtos, GeneratorType))

print(
    list(map(
    lambda x: x * 3,
    [1,2,3,4,5,6,7,8],
    ))
)