'''Já consigo formar a matriz e rotaciona-la, ainda falta conseguir fazer as diagonais'''

numeros = list()
camadas = list()
linhas = list()
colunas = list()

t = 3

for c in range(0, t**3, 1):  # Números para matrizes
    numeros.append(c)

# Formação da Matriz

for c1 in range(0, t):
    for c2 in range(0, t):
        for c3 in range(0, t):
            colunas.append(numeros[0])
            numeros.remove(numeros[0])
        linhas.append(colunas[:])
        colunas.clear()
    camadas.append(linhas[:])
    linhas.clear()

matriz = list(camadas[:])

maior = len(str(matriz[-1][-1][-1]))

# Rotações do cubo

# x = y = z = 0
# print(camadas)
# cam = [camadas[x][z][y],camadas[z][y][x],camadas[y][x][z],
#        camadas[x][y][z],camadas[z][x][y],camadas[y][z][x]]

for z in range(0, t):  # CAMADAS
    for y in range(0, t):  # LINHAS
        for x in range(0, t):  # COLUNAS
            print(f'[{matriz[y][x][z]:>{maior}}]', end=' ')
        print()
    print()

# x y z -> x+1 y+1 z+1 
# x y z -> x+1 y-1 z+1
# x y z -> x-1 y+1 z+1
# x y z -> x+1 y-1 z+1

# Valores da camada inicial

diagonaisinicio = []

# x, y, z
for z in range(0, t):
    for y in range(0, t):
        for x in range(0, t):
            if z == 0:
                diagonaisinicio.append([z, y, x])


diagonal_1 = []

diagonal_temporaria_1 = []

# print(f'Início de cada Diagonal: {diagonaisinicio}')

for iD in diagonaisinicio:
    z = iD[0]
    y = iD[1]
    x = iD[2]
    for k in range(0, t):
        # print(f'{matriz[z][y][x]:>{maior}}', end=' ')
        diagonal_temporaria_1.append(matriz[z][y][x])
        if z == t-1:
            diagonal_1.append(diagonal_temporaria_1[-1:-t-1:-1])
            diagonal_temporaria_1.clear
            # print('\n')
        z += 1
        y += 1
        x += 1
        if z > t-1:
            z = 0
        if y > t-1:
            y = 0
        if x > t-1:
            x = 0

print(diagonal_1)

#       \           \           \           \

diagonal_2 = []

diagonal_temporaria_2 = []

# print(f'Início de cada Diagonal: {diagonaisinicio}')

for iD in diagonaisinicio:
    z = iD[0]
    y = iD[1]
    x = iD[2]
    for k in range(0, t):
        # print(f'{matriz[z][y][x]:>{maior}}', end=' ')
        diagonal_temporaria_2.append(matriz[z][y][x])
        if z == t-1:
            diagonal_2.append(diagonal_temporaria_2[-1:-t-1:-1])
            diagonal_temporaria_2.clear
            # print('\n')
        z += 1
        y -= 1
        x += 1
        if z > t-1:
            z = 0
        if y < 0:
            y = t-1
        if x > t-1:
            x = 0

print(diagonal_2)

#       \           \           \           \

diagonal_3 = []

diagonal_temporaria_3 = []

# print(f'Início de cada Diagonal: {diagonaisinicio}')

for iD in diagonaisinicio:
    z = iD[0]
    y = iD[1]
    x = iD[2]
    for k in range(0, t):
        # print(f'{matriz[z][y][x]:>{maior}}', end=' ')
        diagonal_temporaria_3.append(matriz[z][y][x])
        if z == t-1:
            diagonal_3.append(diagonal_temporaria_3[-1:-t-1:-1])
            diagonal_temporaria_3.clear
            # print('\n')
        z += 1
        y -= 1
        x -= 1
        if z > t-1:
            z = 0
        if y < 0:
            y = t-1
        if x < 0:
            x = t-1

print(diagonal_3)

#       \           \           \           \

diagonal_4 = []

diagonal_temporaria_4 = []

# print(f'Início de cada Diagonal: {diagonaisinicio}')

for iD in diagonaisinicio:
    z = iD[0]
    y = iD[1]
    x = iD[2]
    for k in range(0, t):
        # print(f'{matriz[z][y][x]:>{maior}}', end=' ')
        diagonal_temporaria_4.append(matriz[z][y][x])
        if z == t-1:
            diagonal_4.append(diagonal_temporaria_4[-1:-t-1:-1])
            diagonal_temporaria_4.clear
            # print('\n')
        z += 1
        y += 1
        x -= 1
        if z > t-1:
            z = 0
        if y > t-1:
            y = 0
        if x < 0:
            x = t-1

print(diagonal_4)

todas_as_diagonais = diagonal_1 + diagonal_2 + diagonal_3 + diagonal_4

diagonais_primas = []

contador_primo = 0

for diagonais in todas_as_diagonais:  # Cada diagonal individual
    for num in diagonais:  # Cada número da diagonal
        for mul in range(2,num):  # Cada múltiplo no número (desconsidera 1 e ele mesmo)
            if (num % mul == 0):
                contador_primo = 1
    if contador_primo == 0 and 0 not in diagonais:
        diagonais_primas.append(diagonais)
    contador_primo = 0


print(f'\nDiagonais Primas = {diagonais_primas}')

print(diagonaisinicio)