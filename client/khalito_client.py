from datetime import datetime
import logging
from time import sleep
import signal

import Adafruit_DHT as ada
import RPi.GPIO as GPIO

from pg_objects import TemperatureSensor, DaytimeCycle, Relay
from sql import Sql




"""/
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
#        count = -1
#        while count < 3:
        while True:
            #count +=1
            sleep_for = sleep_time()
            self.log.debug(f"Sleeping for {sleep_for} minutes")
            sleep(sleep_for * 60)
            #sleep(60)
            self.log_temps()
            self.check_relays()

        GPIO.cleanup()

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
            self.log.debug("Attempting to get DB connection for relays")
            self.sql = Sql()
        except Exception as e:
            self.log.error(e, exc_info=True)
            return
        self.log.debug("DB connection acquired")
        try:
            daytime = DaytimeCycle(*self.sql.get_daytime())
        except Exception as e:
            self.log.error(e, exc_info=True)
            return
        
        # We have to check for temps and then for day and night
        try:
            relays = self.sql.get_relays()
        except Exception as e:
            self.log.error(e, exc_info=True)
        
        for relay in relays:
            r = Relay(*relay) 
            if r.control == 'light':
                self.log.debug(f"Testing {r}")
                r = self.set_state(r, daytime)
                self.set_gpio(r)




    def set_gpio(self, relay):
        """
        Method uses the GPIO module to activate a GPIO
        """
        self.log.debug("Setting GPIO for usage")
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(relay.gpio, GPIO.OUT)
        self.log.debug("Checking if GPIO needs to be changed")

        # Check if the GPIO does not match our state

        if GPIO.input(relay.gpio) == relay.relay_state:
            self.log.info("GPIO does not need to be changed, cleaning then exiting function")
            #GPIO.cleanup()
            return

        # If the GPIO is different, then action it
        self.log.info(f"Changing {relay} state to {relay.relay_state}")
        GPIO.output(relay.gpio, relay.relay_state)
        #GPIO.cleanup()
        return

    def set_state(self, relay, daytime):
        """
        This method is used to set the relay_state. The relay_state will be used to action the 
        relay
        """
        state = relay.relay_state
        if daytime.daytime:
            if relay.daytime:
                relay.relay_state = True
                self.log.info(f'Set {relay} to True')
            else:
                relay.relay_state = False
                self.log.info(f'Set {relay} to False')
        else:
            if relay.daytime:
                relay.relay_state = False
                self.log.info(f'Set {relay} to False')
            else:
                relay.relay_state = True
                self.log.info(f'Set {relay} to True')

        if state != relay.relay_state:
            self.sql.set_relay_state(relay)

        return relay

def get_logger():
    """
    Set up file logging for the class
    """
    logger = logging.getLogger('root')
    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler(filename=f'khalo.log', encoding='utf-8', mode='w')
    stdout_handler = logging.StreamHandler()
    
    file_handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
    stdout_handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
    logger.addHandler(file_handler)
    logger.addHandler(stdout_handler)
    return logger

def sleep_time():
    """
    Function used to round time to the nearest 5 minutes
    """
    now = datetime.now()
    remainder = now.minute % 5
    return 5 - remainder

def signal_handler(signal, frame):
    GPIO.cleanup()
    exit()


if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    KhaloClient().start()
