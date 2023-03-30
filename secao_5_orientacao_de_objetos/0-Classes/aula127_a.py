# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.

import json

PATH = 'C:\\Users\\danie\\Documents\\curso_python\\udemy_python\\secao_5_orientacao_de_objetos\\0-Classes\\aula127_a.json'

class users:
    def __init__(self, nome, endereco, idade,):
        self.nome = nome
        self.endereco = endereco
        self.idade = idade

dados1 = users('Daniel Barreto', 'Rua sei lá das quantas', 123)

dados2 = users('Fernando Andrade', 'Rua Minha Nossa Senhora', 33)

dados_juntos = [vars(dados1), vars(dados2)]


def fazer_dump():
    with open(PATH, '+tw', encoding='utf8') as arquivo:

        dados_local = json.dump(
            dados_juntos,
            arquivo,
            ensure_ascii=False,
            indent= 2,
        )


if __name__ == '__main__':
    fazer_dump()



