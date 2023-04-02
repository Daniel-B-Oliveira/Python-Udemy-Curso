import accounts, persons, bank
import random, json

PATH = 'C:\\Users\\danie\\Documents\\curso_python\\udemy_python\\secao_5_orientacao_de_objetos\\8-Meta_classe\\aula158\\dados.json'



with open(PATH, 'r', encoding='utf8') as arquivo:
    contas_ja_registradas = json.load(arquivo)

def fazer_dump():
    with open(PATH, '+tw', encoding='utf8') as arquivo:

        dados_local = json.dump(
            contas_ja_registradas,
            arquivo,
            ensure_ascii=False,
            indent= 2,
        )

fazer_dump()


while True:

    nome = input('Digite seu nome: ')
    idade = input('Digite sua idade: ')

    try:
        idade = int(idade)
    except ValueError:
        print('Valor inválido')
        continue

    pergunta = input('Você já possui uma conta? [s] [n]')
    if pergunta == 'n':

        pessoa = persons.Client(nome, idade)

        numero_da_agencia = random.randint(1000,9999)

        numero_da_conta = int(
            str(random.randint(1000000,9999999)) +\
            str(len(contas_ja_registradas)))

        print('Selecione o número do tipo de conta que deseja criar:')
        pergunta = input('[1] conta conrrente,\n'\
                         '[2] poupança')

        if pergunta == '1':
            pessoa.account =  accounts.CheckingAccount(
                numero_da_agencia,
                numero_da_conta,
            )
        elif pergunta == '2':
            pessoa.account = accounts.SavingsAcconut(
                numero_da_agencia,
                numero_da_conta,
            )
        print('Agência:',numero_da_agencia)
        print('Conta', numero_da_conta)

        pessoa.account = vars(pessoa.account)  # type: ignore

        contas_ja_registradas.append(vars(pessoa))

        fazer_dump()

        print(contas_ja_registradas)

        continue

    elif pergunta == 's':
        numero = input('Digite o número da conta: ')
        numero = int(numero[7:])
        ...
