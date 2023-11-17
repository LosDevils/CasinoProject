import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

connection = psycopg2.connect(user="postgres", password="3657")
connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cursor = connection.cursor()
sql_create_database = "create database casino_db"
cursor.execute(sql_create_database)
connection.commit()
