""""
Iterando strings com while
"""

nome = 'Daniel Barreto'

novo_nome = str()

indice = 0

while indice < len(nome):
    if indice == len(nome) - 1:    
        novo_nome += '*' + nome[indice] + '*'
    else:
        novo_nome += '*' + nome[indice]
    indice += 1

print(novo_nome)