import psycopg2
from settings import database_connection

class Sql:
    def __init__(self):
        self.conn = psycopg2.connect(**database_connection)

    def get_daytime(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM temperature_monitor_app_daytimecycle;")
        return cur.fetchone()[:1]