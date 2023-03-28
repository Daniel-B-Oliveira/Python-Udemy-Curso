# Yield from

def gen1():
    print('Começou gen1')
    yield 1
    yield 2
    yield 3
    print('Acabou gen1')


def gen3():
    print('Começou gen3')
    yield 10
    yield 20
    yield 30
    print('Acabou gen3')

def gen2(gen):
    print('Começou gen2')
    yield from gen()
    yield 4
    yield 5
    yield 6
    print('Acabou gen2')


g1 = gen2(gen1)
g2 = gen2(gen3)


for numero in g1:
    print(numero)

for numero in g2:
    print(numero)