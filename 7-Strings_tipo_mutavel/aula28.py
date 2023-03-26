nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
espaco = ' ' in nome


if nome and idade:
    print(f'Se nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    print(f'Seu nome contem espaços? {espaco}')
    print(f'Seu nome contem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')
else:
    print('Desculpe, você deixou campos vazios.')

