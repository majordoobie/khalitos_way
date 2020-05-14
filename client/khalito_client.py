import psycopg2
from settings import database_connection

conn = psycopg2.connect(**database_connection)
cur = conn.cursor()
cur.close()
conn.close()