"""
Introdução às funções (def) em Python
Funções são trechos de código usados para 
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos) 
e retornar um valor específico.
Por padrão, funções Python retornam None (nada).
"""

# def Print(a, b, c):
#     print('varias1')
#     print('varias2')
#     print('varias3')
#     print('varias4')


# def imprimir(a, b, c):
#     print(a,b,c)

# imprimir(1,2,3)

def saudacao(nome='sem nome'):
    print(f'Olá,{nome}.')

saudacao('Daniel Barreto')
saudacao()