'''while/else'''

string = 'Valorqualquer'

i = 0

while i < len(string):
    letra = string[i]

    if letra == ' ':
        break

    print(letra, end='')

    i += 1

    # if i == len(string):
    #     print()
    #     break

else:
    print('Não encontrei \'espaço\' na string')  # caso tenha break no while o else não será executado

print('fora do while')