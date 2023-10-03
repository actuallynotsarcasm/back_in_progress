import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

try:
    connection = psycopg2.connect(user="postgres",
                                  password="Postgres_8614",
                                  host="127.0.0.1",
                                  port="5432")
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = connection.cursor()
    sql_drop_database = 'DROP DATABASE vtb_autocredit'
    cursor.execute(sql_drop_database)
except (Exception, Error) as error:
    print("Ошибка при удалении БД", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print('Соединение закрыто')