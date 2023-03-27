# if / elif      / else
# se / se não se / se não

entrada = input('Você quer "entrar" ou "sair"?')

if entrada == 'entrar':
    print('Você quer entrar')
elif entrada == 'sair':  # Pode ser repetidos diversas vezes
    print('Você quer sair')
else:
    print('Você não digitou "entrar" nem "sair"')
