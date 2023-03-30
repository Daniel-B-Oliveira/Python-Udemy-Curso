# Métodos em instâncias de classes python

# Hard Coded é algo que foi escrito diretamente no carro


# Entendendo self em classes Python
# Classe é o molde (geralmente não tem dados)
# Instância da class (objeto) - Tem os dados
# Uma classe pode gear varias instrâncias
# Na classe o self é a própria instrância


class Carro:
    def __init__(self, nome):
        self.nome = nome
    
    def acelerar(self):
        print(f'{self.nome} está acelerando...')


fusca = Carro('Fusca')
print(fusca.nome)
fusca.acelerar()

celta = Carro('Celta')
print(celta.nome)
celta.acelerar()
