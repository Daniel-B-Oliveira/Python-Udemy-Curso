"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

# numero_str = input('Digite um número inteiro: ')

# try:
#     numero_int = int(numero_str)
#     numero_par = numero_int % 2 == 0

#     if numero_par:
#         print(f'{numero_int} é par')
#     else:
#         print(f'{numero_int} é impar')

# except:
#     print('Isto não é um número inteiro.')


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

# horario_str = input('Digite a hora atual (entre 0 e 23): ')

# try:
#     horario_int = int(horario_str)

#     dia = 0 <= horario_int <= 11 
#     tarde = 12 <= horario_int <= 17
#     noite = 18 <= horario_int <= 23

#     if dia:
#         print('Bom dia!')
#     elif tarde:
#         print('Boa tarde!')
#     elif noite:
#         print('Boa noite!')
#     else:
#         print(f'{horario_int} não é um valor possível')

# except:
#     print(f'Esse valor ({horario_str}) não pode ser considerado uma hora.')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

# primeiro_nome = input('Digite seu primeiro nome: ')
# confirmacao_de_apenas_primeiro_nome = ' ' not in primeiro_nome

# tamanho_nome = len(primeiro_nome)
# if confirmacao_de_apenas_primeiro_nome and tamanho_nome >= 3:

#     nome_curto = tamanho_nome <= 4
#     nome_normal = 5 <= tamanho_nome >= 6
#     nome_grande = tamanho_nome > 6

#     if nome_curto:
#         print('Seu nome é curto')
#     elif nome_normal:
#         print('Seu nome é normal')
#     elif nome_grande:
#         print('Seu nome é muito grande')

# else:
#     print(f'{primeiro_nome}; contém espaços ou tem menos de 3 letras,'
#           f' logo não pode ser considerado como o primeiro nome')
