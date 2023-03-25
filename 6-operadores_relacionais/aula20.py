primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor > segundo_valor:
    print(f'O primeiro valor ({primeiro_valor}) '
          f'é maior que o segundo valor ({segundo_valor})')

elif primeiro_valor < segundo_valor:
    print(f'O segundo valor ({segundo_valor}) '
          f'é maior que o primeiro valor ({primeiro_valor})')

else:
    print(f'Ambas as variáveis ({primeiro_valor,segundo_valor}) '
          f'tem o mesmo valor')
