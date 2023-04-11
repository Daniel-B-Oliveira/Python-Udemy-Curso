import sqlite3
from pathlib import Path

ROOT_FOLRDE = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_FOLRDE / DB_NAME
TABLE_NAME = 'customers'

conneciton = sqlite3.connect(DB_FILE)

# Quem realizada as oprerações no banco de dados
cursor = conneciton.cursor()

# CRUD - Creat   Read  Update    delete
# SQL - INSERT CREAT UPDATE DELETE

# DANGER: fazendo um dele sem wher
cursor.execute(
    f'DELETE FROM {TABLE_NAME}'
)

# DELETE mais cuidadoso
cursor.execute(
    f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"'
)

conneciton.commit

#Criar tabela

cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weight REAL'
    ')'
)

conneciton.commit()

#Registrar valores na coluna
# CUIDADO: valores de usuários/ SQL injection

sql = (
    f'INSERT INTO {TABLE_NAME} '
    '(name, weight) '
    'VALUES '
    '(?, ?)'
)

# cursor.execute(sql, ['Daniel', 4])
cursor.executemany(
    sql, 
    (
        ('Teste1', 9),
        ('Teste2', 8),
        ('Teste3', 7),
        ('Teste4', 6),
        ('Teste5', 5),
        ('Teste6', 4),
        ('Teste7', 3)
    )
)
conneciton.commit()


if __name__ == '__main__':
    print(sql)


    cursor.execute(
        f'DELETE FROM {TABLE_NAME} '
        'WHERE id=3'
    )
    conneciton.commit()
    cursor.execute(
        f'DELETE FROM {TABLE_NAME} '
        'WHERE id=1'
    )
    conneciton.commit()
    cursor.execute(
        f'UPDATE {TABLE_NAME} '
        'SET name="Anything", weight=67.89 '
        'WHERE id=2'
    )
    conneciton.commit()

    cursor.execute(
        f'SELECT * FROM {TABLE_NAME} '
    )
    for row in cursor.fetchall():
        _id, name, weight = row
        print(_id, name, weight)

    cursor.close()
    conneciton.close()