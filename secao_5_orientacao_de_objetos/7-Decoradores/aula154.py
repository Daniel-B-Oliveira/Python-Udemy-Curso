# Classes decoradoras (decorar classes)

class Multiplicar:
    def __init__(self, multiplicador):

        self._multiplicador = multiplicador

    def __call__(self, func):
        def inter(*args,**kwargs):
            result = func(*args,**kwargs)
            return result * self._multiplicador
        return inter

@Multiplicar(10)
def soma(x, y):
    return x + y


dois_mais_dois = soma(2,2)
print(dois_mais_dois)