import os

import pymysql
import dotenv

TALBE_NAME = 'customers'

dotenv.load_dotenv()

connection = pymysql.connect(
    host =os.environ['MYSQL_HOST'],
    user =os.environ['MYSQL_USER'],
    passwd=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE']
)

with connection:
    with connection.cursor() as cursor:
        cursor.execute(
            f'CREATE TABLE IF NOT EXISTS {TALBE_NAME} ('
                'id INT NOT NULL AUTO_INCREMENT, '
                'nome VARCHAR(50) NOT NULL, '
                'idade INT NOT NULL, '
                'PRIMARY KEY (id)'
            ') '
        )
        # LIMPA A TABELA
        cursor.execute(f'TRUNCATE TABLE {TALBE_NAME}')
    connection.commit()

    # Manipulação de dados
    with connection.cursor() as cursor:
        result = cursor.execute(
            f'INSERT INTO {TALBE_NAME} '
                '(nome, idade) VALUES ("Pessoa", 23) '
        )
        print(cursor)
        print(result)
    connection.commit()
        


