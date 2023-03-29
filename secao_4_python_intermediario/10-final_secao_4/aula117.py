import json

# pessoa = {
#   "nome": "Luiz Otávio 2",
#   "sobrenome": "Miranda",
#   "enderecos": [
#     {"rua": "R1","numero": 32},
#     {"rua": "R2", "numero": 55}
#     ],
#     "altura": 1.8,
#     "numeros_preferidos": [2, 4, 6, 8, 10]
# }

# with open('aula117.json', 'w', encoding='utf8') as arquivo:
#     json.dump(
#         pessoa, 
#         arquivo,
#         indent=2,
#         )

# pode alterar algumas formatações de dados

with open('aula117.json', 'r', encoding='utf8') as arquivo:
    pessoa = json.load(arquivo)
    print(pessoa)