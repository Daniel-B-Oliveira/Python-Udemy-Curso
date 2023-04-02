# dataclasses - O que são dataclasses?
# O módulo dataclasses fornece um decorador e funções para criar métodos como
# __init__(), __repr__(), __eq__() (entre outros) em classes definidas pelo
# usuário.
# Em resumo: dataclasses são syntax sugar para criar classes normais.
# Foi descrito na PEP 557 e adicionado na versão 3.7 do Python.
# doc: https://docs.python.org/3/library/dataclasses.html

from dataclasses import dataclass, asdict, astuple, field


@dataclass(init=False,)      # post_init não será executado
class Pessoa:
    nome: str
    sobrenome: str
    # endereco: list[str] = field(default_factory=list)

    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome


    def __post_init__(self):
        print('Pós init')


    @property
    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'
    

    @nome_completo.setter
    def nome_completo(self, valor):
        nome, *sobrenome = valor.split()
        self.nome = nome
        self.sobrenome = ' '.join(sobrenome)


if __name__ == '__main__':
    p1 = Pessoa('Daniel', 'Barreto')
    p1.nome_completo = 'Daniel Barreto de Oliveira'
    print(astuple(p1))
    print(asdict(p1))

