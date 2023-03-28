# isinstace - para sabe se objeto é de determinado tipo

lista = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2),
    {0, 1}, {'nome': 'Daniel'},
]

for item in lista:
    if isinstance(item, set):
        print('SET', end=' - ')
        item.add(5)
        print(item, isinstance(item, set))
    
    elif isinstance(item, str):
        print('STR', end=' - ')
        print(item.upper())
    
    elif isinstance(item, (int, float)):
        print('NUM', end=' - ')
        print(item * 2)
    else:
        print('OUTRO', end=' - ')
        print(item)
