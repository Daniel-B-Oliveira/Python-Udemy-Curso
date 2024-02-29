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
        sql = (
            f'INSERT INTO {TALBE_NAME} '
            '(nome, idade) '
            'VALUES '
            '(%s, %s) '
        )
        
        data = ("Daniel", 18)
        result = cursor.execute(sql,data)
        
        print(sql, data)
        # print(result)
    connection.commit()

    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TALBE_NAME} '
            '(nome, idade) '
            'VALUES '
            '(%(name)s, %(age)s) '
        )
        
        data2 = {
                "age": 143,
                "name": "Josepha",
            }
        result = cursor.execute(sql,data2)
        
        print(sql, data2)
        # print(result)
    connection.commit()

        


