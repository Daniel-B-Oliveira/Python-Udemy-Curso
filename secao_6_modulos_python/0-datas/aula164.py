# Formatando datas do datetime
# datetime.strftime('DATA', 'FORMATO')
# https://docs.python.org/3/library/datetime.html
from datetime import datetime

fmt = '%d/%m/%Y'
# data = datetime(2022, 12, 13, 7, 59, 23)
data = datetime.strptime('2023-12-13 07:59:23', '%Y-%m-%d %H:%M:%S')

print(data.strftime('%d/%m/%Y'))

print(
    data.strftime('%Y').__class__.__name__,\
    data.year.__class__.__name__
    )

