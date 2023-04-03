# Exercício solucionado: calculando as datas e parcelas de um empréstimo
# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela

from datetime import datetime
from dateutil.relativedelta import relativedelta

valor_do_emprestimo = 300_000.23


data_inicial = datetime.strptime('20-12-2020','%d-%m-%Y')

total = (
    (data_inicial + relativedelta(years=1)) - 
    data_inicial).days // 30


parcela = round(valor_do_emprestimo/total,2)

for d in range(total):

    data_print = str(data_inicial.strftime('%m/%d/%Y'))

    mensagem =(
          f'{d+1:0{len(str(total))}}º - '   # Número
          f'{data_print}  : '               # Data
          f' R$ {parcela:,.2f}'             # Valor
          )

    print(mensagem)
    if data_inicial.month == 12:
        print('-'*len(mensagem))

    tempo_2 = relativedelta(months=1)
    data_inicial += tempo_2

