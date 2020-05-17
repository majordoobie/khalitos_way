from datetime import datetime
import logging
import psycopg2
from settings import database_connection

class Sql:
    def __init__(self):
        self.conn = psycopg2.connect(**database_connection)
        self.log = logging.getLogger('root.sql')

    def get_daytime(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM temperature_monitor_app_daytimecycle;")
        try:
            start, end = cur.fetchone()[1:]
        except Exception as e:
            self.log.error(e, exc_info=True)
            return

        cur.close()
        return start, end

    def get_sensors(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM temperature_monitor_app_temperaturesensor;")
        self.log.debug("Getting sensors")
        result = cur.fetchall()
        cur.close()
        return result

    def set_reading(self, sensor):
        cur = self.conn.cursor()
        sql = """INSERT INTO temperature_monitor_app_temperatureread (
            	device_name_id,
                sample_date,
                temperature,
                humidity,
                device_online
            ) VALUES (%s, %s, %s, %s, %s)"""

        cur.execute(sql, (
            sensor.device_name,
            datetime.now().strftime('%H:%M %d%b%y'),
            sensor.temperature,
            sensor.humidity,
            sensor.device_online
        ))
        self.log.debug(f"Temperature {sensor} recorded")
        self.conn.commit()
        cur.close()
        return

    def get_relays(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM temperature_monitor_app_relay;")
        self.log.debug("Getting relays")
        results = cur.fetchall()
        cur.close()
        return results

    def close(self):
        self.conn.close()