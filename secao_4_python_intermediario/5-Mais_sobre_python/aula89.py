# dir, hasattr e getattr em Python

string = 'Daniel'

metodo = 'upper'

if hasattr(string, 'upper'):
    print(f'Existe {metodo}')
    print(getattr(string, metodo)())
else:
    print('Não existe o método', metodo)