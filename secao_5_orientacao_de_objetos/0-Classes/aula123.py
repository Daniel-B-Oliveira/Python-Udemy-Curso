# Escopo da classe e de métodos da classe

class Animal:
    # nome = 'Leão'

    def __init__(self, nome):
        self.nome = nome


    def acao(self):
        return f'{self.nome} está fazendo uma ação.'

leao = Animal(nome='Leão')
print(leao.nome)
print(leao.acao())