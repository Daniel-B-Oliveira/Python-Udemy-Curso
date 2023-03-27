
# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.


def numero_multiplicado(numero):
    def multiplicador(multiplo):
        return(numero * multiplo)
    return multiplicador


for numero in range(1,11):
    fator = numero_multiplicado(numero)
    for multiplo in range(1,5):
        print(f'{numero} X {multiplo} = {fator(multiplo)}')
    print()

