from datetime import datetime
import Logging
from time import sleep

from sql import Sql

conn = psycopg2.connect(**database_connection)
cur = conn.cursor()
cur.close()
conn.close()


"""
- Make sure that you are asking for DHT22 ( 4 pin) or DHT11 (3 pin)
- You just need to ask for GPIO pin cause it'll just need power and ground

Returns:
    [type] -- [description]
"""
class KhaloClient:
    def __init__(self):
        self.log = get_logger()
        self.start()

    def start(self):
        self.log.debug("Starting loop")
        while True:
            sleep_for = sleep_time()
            self.log.debug(f"Sleeping for {sleep_for}")
            sleep(sleep_for)
            log_temps()

    def log_temps(self):
        try:
            self.log.debug("Attempting to get DB connection")
            self.sql = Sql()
        except Exception as e:
            self.log.error(e, exc_info=True)
            return

        self.log.debug("DB connection acquired")
        
def get_logger():
    """
    Set up file logging for the class
    """
    logger = logging.getLogger('root')
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler(filename=f'khalo.log', encoding='utf-8', mode='w')
    handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
    logger.addHandler(handler)
    return logger

def sleep_time():
    """
    Function used to round time to the nearest 5 minutes
    """
    now = datetime.now()
    remainder = now.minute % 5
    return 5 - remainder

def day_time():

   cur.execute("SELECT * FROM temperature_monitor_app_daytimecycle;") 
# cur.execute("SELECT * FROM temperature_monitor_app_temperaturesensor;")
# cur.execute("SELECT * FROM temperature_monitor_app_daytimecycle;") 

if __name__ == '__main__':
    KhaloClient().start()