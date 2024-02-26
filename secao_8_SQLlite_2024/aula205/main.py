import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# CRUD - Creat Read  Update Delete
# SLQ - INSERT SELECT UPDATE DELETE

#CUIDADO: Fazendo o delete sem where

cursor.execute(
    f'DELETE FROM {TABLE_NAME}'
)

#Reinicia o valor dos ids
# DELETE mais cuidadoso
cursor.executescript(
    f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"'
)
connection.commit()


#Cria Tabela
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weight REAL'
    ')'
)
connection.commit()


#Registrar valores nas colunas da tabela

#CUIDADO: sql injection
# sql = (
#     f'INSERT INTO {TABLE_NAME} '
#     '(id, name, weight) '
#     'VALUES '
#     '(NULL, "Daniel Barreto", 9.9), '
#     '(NULL, "Joao", 4) '
# )

sql = (
    f'INSERT INTO {TABLE_NAME} '
    '(name, weight) '
    'VALUES '
    '(:name_customers, :weight_customers) '
)

# cursor.execute(sql, ['Joana',4])

# cursor.executemany(
#     sql,
#     (
#         ('Daniel',4),
#         ('Joana', 5)
#     )
# )

cursor.execute(
    sql,
    {
        'name_customers':'Daniel', 'weight_customers':4
    }
)

cursor.executemany(
    sql,
    (
        {'name_customers':'Customer A', 'weight_customers':1},
        {'name_customers':'Customer B', 'weight_customers':2},
        {'name_customers':'Customer C', 'weight_customers':3},
    )
)

connection.commit()

if __name__ == '__main__':
    print(sql)

    cursor.execute(
        f'DELETE  FROM {TABLE_NAME} '
        'WHERE id = "3" '
    )
    cursor.execute(
        f'DELETE  FROM {TABLE_NAME} '
        'WHERE id = 1 '
    )
    connection.commit()

    cursor.execute(
        f'UPDATE {TABLE_NAME} '
        'SET name = "Customer N", weight = 100 '
        'WHERE id = 2'
    )
    connection.commit()

    
    cursor.execute(
        f'SELECT * FROM {TABLE_NAME}'
    )
    
    for row in cursor.fetchall():
        _id, name, weight = row
        print(_id, name, weight)


    cursor.close()
    connection.close()

