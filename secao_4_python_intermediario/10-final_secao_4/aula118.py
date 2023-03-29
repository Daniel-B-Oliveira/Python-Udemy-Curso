# Problema dos parametros mutáveis em funções Python

def adiciona_clientes(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista


cliente_1 = adiciona_clientes('Daniel',)
adiciona_clientes('Joana', cliente_1)
adiciona_clientes('Fernando', cliente_1)
print(cliente_1)


cliente_2 = adiciona_clientes('Helena')
adiciona_clientes('Maria', cliente_2)
print(cliente_2)
