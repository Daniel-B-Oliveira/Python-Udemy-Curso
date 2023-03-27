"""
argumentos nomeados e não nomeados em funções python
argumento nomeado tem nome com sinal de igual
argumento não nomeado recebe apenas o argumento (valor)
"""

def soma(x, y,z):
    # Definição
    print(f'{x=} {y=} {z=}', '|', 'x + y + z =', x+y+z)

soma(1,2,3)
soma(1, y = 2, z = 3)
soma(y=2,x=1,z=3)