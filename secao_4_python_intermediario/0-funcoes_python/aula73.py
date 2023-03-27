"""
Higher Order Functions

Funções de primeira classe
"""

# def saudacao(msg):

#     return(msg)


# def executa(funcao):
#     return funcao()


# saudacao_2 = saudacao

# v = executa(saudacao)



def saudacao(msg='<none>', nome='<none>'):
    return f'{msg}, {nome}'


def executa(funcao, *args):
    return funcao(*args)


print(
    executa(saudacao, 'Bom dia', 'Daniel')
)

print(
    executa(saudacao, 'Bom dia')
)

print(
    executa(saudacao)
)
