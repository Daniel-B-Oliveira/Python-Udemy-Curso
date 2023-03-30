
import json
from aula127_a import PATH, users, fazer_dump

fazer_dump()

with open(PATH, 'r', encoding='utf8') as arquivo:
    dados = json.load(arquivo)
    p1 = users(**dados[0])
    p2 = users(**dados[1])


    print(p1.nome)
    print(p2.nome)
