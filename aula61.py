"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10
Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0
Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O primeiro dígito do CPF é 7
"""

while True:
    cpf = input('Digite um cpf: ')              #'746.824.890-70'  # input  74682489070

    try:
        cpf_tratado = int(cpf)
    except:
        cpf_tratado_str = cpf[:].replace('.','').replace('-','')
        cpf_tratado = int(cpf_tratado_str)

    if len(str(cpf_tratado)) != 11:
        print('QUantidade de números incompativeis.')
        continue

    valor_soma = 0

    for indice,numero in enumerate(str(cpf_tratado)):
        indice = int(indice)
        numero = int(numero)

        if indice == 9:
            break

        valor_soma += int((10-indice) * numero)

    dig_1 = (valor_soma * 10) % 11
    valor_mudulo = dig_1 if dig_1 < 10 else 0 

    if str(dig_1) == (str(cpf_tratado))[-2]:
        print('Valor Aceito')
    else:
        print('Valor NÃO Aceito')
