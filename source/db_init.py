import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

from schemas import Base, engine

try:
    connection = psycopg2.connect(user="postgres",
                                  password="Postgres_8614",
                                  host="127.0.0.1",
                                  port="5432")
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = connection.cursor()
    sql_create_database = 'CREATE DATABASE vtb_autocredit'
    cursor.execute(sql_create_database)
except (Exception, Error) as error:
    print("Ошибка при создании БД", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print('Соединение закрыто')

Base.metadata.create_all(engine)