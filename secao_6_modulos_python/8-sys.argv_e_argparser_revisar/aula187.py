# sys.argv - Executando arquivos com argumentos no sistema
# Fonte = Fira Code
import sys

argumentos = sys.argv

qtd_argumentos = len(argumentos)

if qtd_argumentos <= 1:
    print('Você não passou argumetos')

else:
    print('Você passou os argumentos', argumentos[1:])

    