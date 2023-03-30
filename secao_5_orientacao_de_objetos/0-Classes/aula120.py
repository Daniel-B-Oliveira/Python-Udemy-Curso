# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.
# string = 'Luiz'  # str
# print(string.upper())
# print(isinstance(string, str))

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
        ...

p1 = Pessoa('Daniel', 'Barreto')
# p1.nome = 'Daniel' # type: ignore
# p1.sobrenome = 'Barreto' # type: ignore

p2 = Pessoa('Maria', 'Joana')
# p2.nome = 'Daniel 2' # type: ignore
# p2.sobrenome = 'Barreto 2' # type: ignore


print(p1.nome) # type: ignore # type: ignore
print(p1.sobrenome) # type: ignore # type: ignore

print(p2.nome) # type: ignore
print(p2.sobrenome) # type: ignore