# Empacotamento e desempacotamento de dicionários
a, b = 1, 2

a, b = b, a
# print(a, b)

# (a1, a2), (b1,b2) = pessoa.items()

# print(a1, a2)
# print(b1, b2)

# for chave, valor in pessoa.items():
#     print(chave, pessoa)

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}

pessoa_completa = {**pessoa, **dados_pessoa}

# print(pessoa_completa)

# args e kwargs
# args (já vimos)
# kwargs - keyword arguments (argumetnos nomeados)

# def mostro_argumentos_nomeados(*args, **kwargs):
#     print('NÃO NOMEADOS:', args)
#     for chave, valor in kwargs.items():
#         print(f'{chave}: {valor}')

# # mostro_argumentos_nomeados(1,2,3,4,nome='Joana', qlq=123)
# mostro_argumentos_nomeados(list(range(10)),**pessoa, **dados_pessoa)
