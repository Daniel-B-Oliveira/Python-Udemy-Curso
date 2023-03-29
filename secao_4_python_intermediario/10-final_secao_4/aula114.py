# Funções recursivas e recursividade
# - funções que podem se chamar de volta
# - úteis p/ dividir problemas grandes em partes menores
# Toda função recursiva deve ter:
# - Um problema que possa ser dividido em partes menores
# - Um caso recursivo que resolve o pequeno problema
# - Um caso base que para a recursão
# - fatorial - n! = 5! = 5 * 4 * 3 * 2 * 1 = 120
# https://brasilescola.uol.com.br/matematica/fatorial.htm

# def recursive(ini=0, end=10):       # Possuim limites, pois todo o escopo é salvo na memoria
#     if ini >= end:
#         return end

#     ini += 1
#     return recursive(ini, end)

# print(recursive())

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(factorial(10))
# print(factorial(1000))  # excede o limite de recursão

numero = 10000

acomulador = 1

for n in range(1,numero+1):
    acomulador *= n

print(acomulador)

