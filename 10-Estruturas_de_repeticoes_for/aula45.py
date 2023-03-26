"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""


# numeros = range(0, 100, 8)

# for numro in numeros:
#     print(numro)


# for letra in texto:  ("!!!for equivale a esta operação!!!")

texto = 'Daniel'
iterator = iter(texto)  # texto.__iter__()       # Interável:

print(next(iterator))      # print(iterator.__next__())   # Iterator:

while True:
    try:
        letra = next(iterator)
        print(letra)
    except StopIteration:
        break
