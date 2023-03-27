# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.


def mult(*numero):
    multiplicacao = 1
    for n in numero:
        multiplicacao *= n
    return multiplicacao

numeros_1 = 1, 2, 3, 4, 5, 6

print(mult(*numeros_1))

numeros_2 = mult(1,2,3,4,5,6)
print(numeros_2)


# Crie um função que fala se o numero é par ou impar
# Retorna se o numero é par ou impar


def par_impar(*numeros):
    impar = ['Impar']
    par = ['Par']
    for valor in numeros:
        if valor % 2 == 0:
            par.append(valor)
        else:
            impar.append(valor)
    if len(impar) == 1:
        impar = []
    if len(par) == 1:
        par = []
    resposta = impar+par
    return resposta


print(par_impar(2))

valor = 1,2,3,4,5,6,
prg = par_impar(*valor)
print(prg)
