
# ANO_ATUAL = 2023

class Pessoa():
    ano_atual = 2023

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade

p1 = Pessoa('João', 31)


# p1.nome = 'JoÃO 2'
# print(p1.nome)

# p1.__dict__['nome'] = 'João 2'
# p1.__dict__['novo'] = 'João Novo'

dado = {'idade': 35, 'nome': 'Marcos'}
p1 = Pessoa(**dado)

print(p1.__dict__)
print(vars(p1))
# print(p1.novo)