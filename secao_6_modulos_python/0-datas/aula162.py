# Criando datas com módulo datetime
# datetime(ano, mês, dia)
# datetime(ano, mês, dia, horas, minutos, segundos)
# datetime.strptime('DATA', 'FORMATO')
# datetime.now()
# https://pt.wikipedia.org/wiki/Era_Unix
# datetime.fromtimestamp(Unix Timestamp)
# https://docs.python.org/3/library/datetime.html
# Para timezones
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# Instalando o pytz
# pip install pytz types-pytz

from datetime import datetime

from pytz import timezone
# data_str_data = '2022/04/02 2:19:23'
# data_str_formato = '%Y/%m/%d %H:%M:%S'

# # data = datetime(2023, 4, 2, 14, 16, 23)

# data = datetime.strptime(data_str_data, data_str_formato)


data = datetime.now(timezone('Asia/Tokyo'))


# Compactação na base de dados :
# a = data.timestamp()
# a = datetime.fromtimestamp(a)
# print(a)

print(data)

