import importlib

import aula98_m

print(aula98_m.variavel)

# for i in range(10):
#     import aula98_m  # todos os modulos são single, só pode ser importado uma vez no programa.

for i in range(10):
    importlib.reload(aula98_m)

print('FIm')

