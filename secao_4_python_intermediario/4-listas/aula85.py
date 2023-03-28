lista = []
for x in range(3):
    for y in range(3):
        lista.append((x, y))

lista = [
    (z, y, x)
    for z in range(3)
    for x in range(3)
    for y in range(3)
]
lista = [
    [(x,letra) for letra in 'Daniel']
    for x in range(3)
]
print(lista)

