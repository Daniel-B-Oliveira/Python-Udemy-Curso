# Dicionários em Python (tipo dict)
# Dicionários são estruturas de dados do tipo
# par de "chave" e "valor".
# Chaves podem ser consideradas como o "índice"
# que vimos na lista e podem ser de tipos imutáveis
# como: str, int, float, bool, tuple, etc.
# O valor pode ser de qualquer tipo, incluindo outro
# dicionário.
# Usamos as chaves - {} - ou a classe dict para criar
# dicionários.
# Imutáveis: str, int, float, bool, tuple
# Mutável: dict, list
# pessoa = {
#     'nome': 'Luiz Otávio',
#     'sobrenome': 'Miranda',
#     'idade': 18,
#     'altura': 1.8,
#     'endereços': [
#         {'rua': 'tal tal', 'número': 123},
#         {'rua': 'outra rua', 'número': 321},
#     ]
# }



# pessoa = {
#     'nome': 'Daniel Barreto',
#     'sobrenome': 'Oliveira',
#     'idade': 18,
#     'altura': 1.72,
#     'enderecos': [
#     {'rua': 'tal número', 'numero': 123},
#     {'rua': 'outra rua', 'numero': 321 },
#     ]
# }

# # pessoa = dict(nome= 'Daniel Barreto', sobrenome = 'Barreto')  # Menos Usado

# # print(pessoa['nome'])
# # print(pessoa['enderecos'])

# for key in pessoa:
#     print(key, pessoa[key])

pessoa = {}


##
##

key = 'nome legal'  # Chave dinâmica

pessoa[key] = 'Daniel Barreto'
# pessoa['TESTE'] = 'TESTE'

# pessoa[key] = 'Troca'
# del pessoa['TESTE']


# if pessoa.get('sobrenome') is not None:
#     print('A chave existe')
# else:
#     print('A chave não existe') 

print(pessoa)
print(pessoa[key])