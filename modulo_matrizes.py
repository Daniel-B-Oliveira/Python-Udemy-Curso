def gerar_numeros(i=0,f=1,c=1):
    numeros = list()

    for n in range(i,f,c):
        numeros.append(n)

    return numeros


def formar_matriz_3d(tamanhho=0):

    numeros_list = gerar_numeros(f=tamanhho**3)

    matrizes_list = list()
    camadas_list = list()
    linhas_list = list()
    colunas_list = list()
        
    for c1 in range(0, tamanhho):
        for c2 in range(0, tamanhho):
            for c3 in range(0, tamanhho):
                colunas_list.append(numeros_list[0])
                numeros_list.remove(numeros_list[0])
            linhas_list.append(colunas_list[:])
            colunas_list.clear()
        camadas_list.append(linhas_list[:])
        linhas_list.clear()
    matrizes_list = camadas_list[:]

    return matrizes_list


def printar_matriz_3d(lista=list('None')):

    tamanho_maior_valor = len(str(lista[-1][-1][-1]))

    for z in range(0, len(lista)):  # CAMADAS
        for y in range(0,  len(lista)):  # LINHAS
            for x in range(0,  len(lista)):  # COLUNAS
                print(f'[{lista[y][x][z]:>{tamanho_maior_valor}}]', end=' ')
            print()
        print()


def coordenada_diagonais_iniciais_matriz_3d(lista=list('None')):
    coodenadas_diagonais = list()
    tamanho = int(len(lista))
    for z in range(0,tamanho):
        for y in range(0,tamanho):
            for x in range(0,tamanho):
                if z == 0:
                    coodenadas_diagonais.append([z, y, x])

    return coodenadas_diagonais


def diagonais_matriz_3d(lista=list('None')):
    tamanho = len(lista)
    diagonais_inicio = coordenada_diagonais_iniciais_matriz_3d(lista)


    diagonal_temporaria = list()

    diagonal_1 = list()
    diagonal_2 = list()
    diagonal_3 = list()
    diagonal_4 = list()

    todas_as_diagonais_list = [diagonal_1,diagonal_2,diagonal_3,diagonal_4]

    for diagonal_n in todas_as_diagonais_list:
        for coodenada in diagonais_inicio:
            z = coodenada[0]
            y = coodenada[1]
            x = coodenada[2]
            for k in range(0, tamanho):
                # print(f'{matriz[z][y][x]:>{maior}}', end=' ')
                diagonal_temporaria.append(lista[z][y][x])
                if z == tamanho-1:
                    diagonal_n.append(diagonal_temporaria[-1:-tamanho-1:-1])
                    diagonal_temporaria.clear
                    # print('\n')
                if diagonal_n == todas_as_diagonais_list[0]:
                    z += 1
                    y += 1
                    x += 1
                    if z > tamanho-1:
                        z = 0
                    if y > tamanho-1:
                        y = 0
                    if x > tamanho-1:
                        x = 0
                elif diagonal_n == todas_as_diagonais_list[1]:
                    z += 1
                    y -= 1
                    x += 1
                    if z > tamanho-1:
                        z = 0
                    if y < 0:
                        y = tamanho-1
                    if x > tamanho-1:
                        x = 0
                elif diagonal_n == todas_as_diagonais_list[2]:
                    z += 1
                    y -= 1
                    x -= 1
                    if z > tamanho-1:
                        z = 0
                    if y < 0:
                        y = tamanho-1
                    if x < 0:
                        x = tamanho-1
                elif diagonal_n == todas_as_diagonais_list[3]:
                    z += 1
                    y += 1
                    x -= 1
                    if z > tamanho-1:
                        z = 0
                    if y > tamanho-1:
                        y = 0
                    if x < 0:
                        x = tamanho-1

        for diagonal_n in todas_as_diagonais_list:
            for cada_diagonal in diagonal_n:
                cada_diagonal.sort()

    return todas_as_diagonais_list


def diagonais_primas(lista=list('None')):

    diagonais_primas = list()

    for diagonal_tipo_n in lista:  # Diagonal 1, 2, 3 ou 4
        for diagonais in diagonal_tipo_n:  # Cada diagonal individual
            for numeros in diagonais:  # Cada número da diagonal
                for multiplos in range(2, numeros):  # Cada antecessor do número (desconsidera 1 e ele mesmo)
                    if (numeros % multiplos == 0):  # Se for divisível, a diagonal inteira não é prima
                        contador_primo = 1
            if contador_primo == 0 and 0 not in diagonais:
                diagonais_primas.append(diagonais)
            contador_primo = 0

    return diagonais_primas

diagonal = diagonais_matriz_3d(formar_matriz_3d(tamanhho=4))

for cada_diag in diagonal:
    print(cada_diag)

print(f'Diagonais primas: {diagonais_primas(diagonal)}')
