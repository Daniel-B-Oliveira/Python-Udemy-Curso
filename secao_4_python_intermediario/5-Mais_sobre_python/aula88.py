# Valores Truthy e Falsy, tipos mutaveis e Imutaveis
# Mutaveis [] {} ser()
# Imutaveis () "" 0 0.0 None False range(0,10)

lista = []
dicnionario = {}
conjunto = set()
tupla = ()
string = ''
inteiro = 0
flutuante = 0.0
nada = None
falso = False
intervalo = range(0)

def falsy(valor):
    return 'falsy' if not valor else 'truthy'

print(f'Teste', falsy('Teste'))
print(f'{lista=}', falsy(lista))
print(f'{dicnionario=}', falsy(dicnionario))
print(f'{conjunto=}', falsy(conjunto))
print(f'{tupla=}', falsy(tupla))
print(f'{string=}', falsy(string))
print(f'{inteiro=}', falsy(inteiro))
print(f'{flutuante=}', falsy(flutuante))
print(f'{nada=}', falsy(falso))
print(f'{falso=}', falsy(falso))
print(f'{intervalo=}', falsy(intervalo))