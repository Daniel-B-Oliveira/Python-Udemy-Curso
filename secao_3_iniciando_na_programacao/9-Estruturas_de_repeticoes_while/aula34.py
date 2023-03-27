"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> quanod um código não ten fim
"""

condicao = True

while condicao:
    nome = input('Qual o seu nome: ')
    if nome == 'sair':
        break
    print(f'Seu nome é {nome}')

print('Acabou')