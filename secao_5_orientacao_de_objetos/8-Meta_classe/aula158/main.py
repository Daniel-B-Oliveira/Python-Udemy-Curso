import accounts, persons, bank
import random, json

PATH = 'C:\\Users\danie\\Documents\\curso_python\\udemy_python\\secao_5_orientacao_de_objetos\\8-Meta_classe\\aula158\\dados.json'

contas_ja_registradas = list()


print(contas_ja_registradas)


while True:

    pessoa = persons.Person(input('Digite seu nome: '), \
                            input('Digite sua idade: '))

    pergunta = input('Você já possui uma conta? [s] [n]')
    if pergunta == 'n':

        numero_da_conta = random.randint(1000000,9999999)
        numero_da_agencia = random.randint(1000,9999)

        print('Selecione o número do tipo de conta que deseja criar:')
        pergunta = input('[1] conta conrrente,\n'\
                         '[2] poupança')
  
        if pergunta == '1':
            conta = accounts.CheckingAccount(
                numero_da_agencia,
                numero_da_conta,
            )
        elif pergunta == '2':
            conta = accounts.SavingsAcconut(
                numero_da_agencia,
                numero_da_conta,
            )
        print('Agência:',numero_da_agencia)
        print('Conta', numero_da_conta)
    elif pergunta == 's':
        ...