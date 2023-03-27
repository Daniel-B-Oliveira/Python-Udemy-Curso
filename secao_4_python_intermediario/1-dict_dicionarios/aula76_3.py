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


# import copy

# d1= {
#     'c1': 1,
#     'c2': 2,
#     'l1': [0, 1, 2]  # shallow copy, ambos os dicionarios se referem a mesma lista (l1)
# }

# # d2 = d1.copy() # == copy.copy(d1)
# d2 = copy.deepcopy(d1)

# d2['c1'] = 1000
# d2['l1'][1] = 999999  # shallow copy

# print(d1,d2)


#           /           /           /           /           /           /


p1 = {
    'Nome': 'Daniel Barreto',
    'Sobrenome': 'Barreto',
}

# print(p1['Nome'])
# print(p1.get('Nome', 'não existe'))

# ultimo_nome = p1.popitem()
# print(ultimo_nome)

# p1.update({
#     'Nome': 'Novo valor',
# })

# p1.update(Nome= 'Novo valor', Sobrenome= 'Novo Sobrenome')

tupla = ('Nome', 'novo valor'),   # funciona para listar tbm
p1.update(tupla)



print(p1)

