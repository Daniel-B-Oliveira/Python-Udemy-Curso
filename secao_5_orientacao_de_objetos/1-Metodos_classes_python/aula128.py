# Métodos de classe + factories (fábricas)
# São métodos onde "self" será "cls", ou seja,
# ao invés de receber a instância no primeiro
# parâmetro, receberemos a própria classe.

class Pessoa:
    ano = 2023  # Atributo de classe

    def __init__(self, nome, idade, ):
        self.nome = nome
        self.idade = idade


    # "EXTENSÃO DA CLASSE" método


    @classmethod
    def metodo_de_calsse(cls):
        print('hi')

    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)
    
    @classmethod
    def criar_sem_nome(cls, idade):
        return cls('<anonima>', idade)


p1 = Pessoa('João', '123')

p2 = Pessoa.criar_com_50_anos('Helena')

p3 = Pessoa.criar_sem_nome(50)

print(p1.nome, p1.idade)
print(p2.nome, p2.idade)
print(p3.nome, p3.idade)