"""
lista de listas e seus indices
"""

salas = [
    ['Maria', 'Helena'],
    ['Elaine'],
    ['Luiz', 'João', 'Eduarda',], #(10,20,30,40,50)],
]

# print(sala[2][3][4])

for sala in salas:
    print(f'A sala é {sala}')
    for aluno in sala:
        print(aluno)