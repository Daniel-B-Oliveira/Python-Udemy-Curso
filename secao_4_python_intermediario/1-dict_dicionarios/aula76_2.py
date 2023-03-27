# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro


pessoa = {
    'nome': 'Daniel Barreto',
    'sobrenome': 'Oliveira',
    'idade': 18,
    'altura': 1.72,
}           # Se os nomes forem iguas , das chaves, o útimo valor será considerado


pessoa.setdefault('idade123', None)
print(pessoa['idade123'])


# # print(pessoa.__len__())  # complicado
# # print(len(pessoa))
# # print(list(pessoa.keys()))     # retorna as chaves
# # print(list(pessoa.values()))     # retorna os valores
# print(list(pessoa.items()))     # retorna os valores

# for chave,valor in pessoa.items():      # Igual ao enumerate, so que para dict
#     print(chave,valor)

