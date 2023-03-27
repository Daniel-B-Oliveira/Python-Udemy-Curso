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

    # Validação do valor

    cpf = input('Digite um cpf: ')              #'746.824.890-70'  # input  74682489070

    try:
        cpf_tratado = int(cpf)

    except:
        cpf_tratado_str = cpf[:].replace('.','').replace('-','')
        cpf_tratado = int(cpf_tratado_str)

    if len(str(cpf_tratado)) != 11:
        print('QUantidade de números incompativeis.')
        continue
    
    # Resultado do primeiro e segundo digito

    for digito in range(1,3):  # Primeiro, depois segundo

        valor_soma = 0

        for indice,numero in enumerate(str(cpf_tratado)):

            indice = int(indice)
            numero = int(numero)

            if indice == 8 + digito:  # Primeiro vira 9, depois vira 10
                break

            valor_soma += int((9+digito-indice) * numero)

        if digito == 1:
            dig_1 = (valor_soma * 10) % 11
            valor_mudulo_1 = dig_1 if dig_1 < 10 else 0 

        elif digito == 2:
            dig_2 = (valor_soma * 10) % 11
            valor_mudulo_2 = dig_2 if dig_2 < 11 else 0 

    aceito_primeiro = str(valor_mudulo_1) == (str(cpf_tratado))[-2] 
    aceito_segundo = str(valor_mudulo_2) == (str(cpf_tratado))[-1]


    if aceito_primeiro and aceito_segundo:
        print('CPF válido')
    else:
        print('Valor NÃO Aceito')


