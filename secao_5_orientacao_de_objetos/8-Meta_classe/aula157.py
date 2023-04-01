# Enum -> Enumerações
# Enumerações na programação, são usadas em ocasiões onde temos
# um determinado número de coisas para escolher.
# Enums têm membros e seus valores são constantes.
# Enums em python:
#   - são um conjunto de nomes simbólicos (membros) ligados a valores únicos
#   - podem ser iterados para retornar seus membros canônicos na ordem de
#       definição
# enum.Enum é a superclasse para suas enumerações. Mas também pode ser usada
#   diretamente (mesmo assim, Enums não são classes normais em Python).
# Você poderá usar seu Enum com type annotations, com isinstance e
# outras coisas relacionadas com tipo.
# Para obter os dados:
# membro = Classe(valor), Classe['chave']
# chave = Classe.chave.name
# valor = Classe.chave.value

import enum
# Mais confuso: 
# Directions = enum.Enum('Dirctions', ['LEFT', 'RIGTH', 'UP', 'DOWN'])  

# print(Directions(1), Directions['LEFT'], Directions.LEFT, sep= ' = ')


class Directions(enum.Enum):
    LEFT = enum.auto()
    RIGTH = enum.auto()
    UP = enum.auto()
    DOWN = enum.auto()

def move(direct: Directions):
    if not isinstance(direct, Directions):
        raise ValueError('Direction not found')

    print(f'Moving {direct.name}, ({direct.value})')

move(Directions.LEFT)
move(Directions.RIGTH)
move(Directions.UP)
move(Directions.DOWN)
