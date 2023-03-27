from random import randint

cpf_valido = []

while True:

    nove_digitos = []

    i = input('Digite o número de cpfs que serã feitos: ')
    try:
        i = int(i)
        break
    except:
        print('Esta string não pod ser transformada em um número inteiro')
        continue

while len(cpf_valido) < i:

    nove_digitos_provisorio= ''

    for c in range(9):
        nove_digitos_provisorio += str(randint(0,9))

    if nove_digitos_provisorio not in nove_digitos:
        nove_digitos.append(nove_digitos_provisorio[:])
    else:
        continue
        
    contador_regressivo_1 = 10

    resultado_digito_1 = 0

    for digito in nove_digitos_provisorio:
        resultado_digito_1 += int(digito) * contador_regressivo_1
        contador_regressivo_1 -= 1
    digito_1 = (resultado_digito_1 * 10) % 11
    digito_1 = digito_1 if digito_1 <= 9 else 0

    dez_digitos = nove_digitos_provisorio + str(digito_1)

    contador_regressivo_2 = 11

    resultado_digito_2 = 0

    for digito in dez_digitos:
        resultado_digito_2 += int(digito) * contador_regressivo_2
        contador_regressivo_2 -= 1
    digito_2 = (resultado_digito_2 * 10) % 11
    digito_2 = digito_2 if digito_2 <= 9 else 0

    cpf_gerado_pelo_calculo = f'{nove_digitos_provisorio}{digito_1}{digito_2}'

    cpf_valido.append(cpf_gerado_pelo_calculo[:])


contador_print = 0

for cpf in cpf_valido:
    print(cpf[0:3]+'.'+cpf[3:6]+'.'+cpf[6:9]+'-'+cpf[9:], end=' ; ')
    contador_print += 1
    if contador_print == 5:
        print()
        contador_print = 0
