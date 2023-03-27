# Exercício - sistema de perguntas e respostas

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

acertos = 0

for indice_pergunta,pergunta in enumerate(perguntas):
    
    print(f'\n{indice_pergunta}) {pergunta["Pergunta"]}\n')

    for indice_alternativa,alternativas in enumerate(pergunta['Opções']):
        print(f'{indice_alternativa}) {alternativas}')

    while True:
        alternativa_escolhida = input('Digite o indice de uma das alternativas: ')
        try:
            alternativa_escolhida = \
            pergunta['Opções'][int(alternativa_escolhida)]
            break
        except IndexError:
            print('\nPor favor, digite uma alternativa existente\n')
            continue
        except ValueError:
            print('\nPor favor, digite um número\n')
    
    if alternativa_escolhida == pergunta['Resposta']:
        print('\nPARABÉNS, você acertou\n')
        acertos += 1
    else:
        print(
            f'\nQue pena, você errou,'
            f' a alternativa certa era'
            f' \'{pergunta["Resposta"]}\'\n')
    
print(f'Fim de jogo, você acertou {acertos}/{len(pergunta)} perguntas')

