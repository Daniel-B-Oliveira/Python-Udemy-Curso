"""
Introdução ao desempacotamento + tuple (tuplas)
"""


# nome1, *resto = ['Maria', 'Helena', 'Luiz']
# nome1, *_= ['Maria', 'Helena', 'Luiz']
_, nome2, *_= ['Maria', 'Helena', 'Luiz']

print(nome2)