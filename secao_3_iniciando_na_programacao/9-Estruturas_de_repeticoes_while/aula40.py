"""CALCULADORA COM WHILE"""

while True:
    numero_1 = input('\nDigite um numero: ')
    numero_2 = input('Digite outro numero: ')
    operador = input('Digite um operador (+-*/): ')

    numero_valido = None  # Não obrigatório

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numero_valido = True  # Não obrigatório

    except:  # Não obrigatório
        numero_valido = None
    
    if numero_valido is None:
        print('Um ou ambos os números digitados são inválidos')
        continue

    operador_permitido = '+-*/'

    if operador not in operador_permitido or len(operador) != 1:
        print('\nOperador inválido')
        continue

    print('Resultado: ',end='')   

    if operador == '+':
        print(num_1_float + num_2_float, '\n')
    elif operador == '-':
        print(num_1_float - num_2_float, '\n') 
    elif operador == '*': 
        print(num_1_float * num_2_float, '\n')
    elif operador == '/': 
        print(num_1_float / num_2_float, '\n')
    else:
            print('\nerro')


    sair = input('\nQuer sair? [s]sim: ').lower().startswith('s')
    if sair:
        break