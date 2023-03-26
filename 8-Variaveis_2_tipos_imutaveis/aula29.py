'''
introdução ao try/except
try -> tentar executar o cógico
except -> ocorreu algum erro ao tentar executar
'''

# Esta maneira de uso do try except não é a idela 
# Está sendo usada apenas para meios didáticos.

numero_str = input(
    'Vou dobrar o número que você digitar: '
)

try:
    numero_float = float(numero_str)
    print(f'O dobro de {numero_str} é {numero_float*2}')
except:
    print(f'Isso não é um número ({numero_str})')