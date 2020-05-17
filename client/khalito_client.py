from datetime import datetime
import logging
from time import sleep

import Adafruit_DHT as ada
import RPi.GPIO as GPIO

from pg_objects import TemperatureSensor, DaytimeCycle, Relay
from sql import Sql


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
        count = 0
        while count < 5:
            count +=1
            sleep_for = sleep_time()
            self.log.debug(f"Sleeping for {sleep_for}")
            #sleep(sleep_for)
            sleep(1)
            self.log_temps()
            self.check_relays()

    def log_temps(self):
        """
        Method is used to log the temperatures to the database, no other actions happen here.
        """
        try:
            self.log.debug("Attempting to get DB connection")
            self.sql = Sql()
        except Exception as e:
            self.log.error(e, exc_info=True)
            return

        self.log.debug("DB connection acquired")
        # Get all sensors from db
        sensors_list = self.sql.get_sensors()
        for sensor in sensors_list:
            # Get sensor object
            s = TemperatureSensor(*sensor)
            # Read the sensor
            humidity, temperature = ada.read_retry(s.sensor_type, s.gpio)
            s.humidity = humidity
            s.temperature = (temperature * 1.8 + 32)
            if s.humidity:
                s.device_online = True
            # Commit the data
            self.sql.set_reading(s)
        # Close connection to the database
        self.sql.close()

    def check_relays(self):
        try:
            self.log.debug("Attempting to get DB connection")
            self.sql = Sql()
        except Exception as e:
            self.log.error(e, exc_info=True)
            return
        try:
            daytime = DaytimeCycle(*self.sql.get_daytime())
        except Exception as e:
            self.log.error(e, exc_info=True)
            return
        
        # We have to check for temps and then for day and night
        relays = self.sql.get_relays()
        for relay in relays:
            r = Relay(*relay) 
            if r.daytime != daytime.daytime:
                

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