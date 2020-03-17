import asyncio
import datetime

import Adafruit_DHT as ada
from aiohttp import web
import RPi.GPIO as GPIO

# TODO Lights on at 0700 with temps at 90-95(HOT)/80-85(COOL)
# TODO Lights off at 1900 with temps at 70-75
# TODO Create a time setter 

class Profile_Setter:
    def __init__(self):
        # Initialize what is day and what is night
        self.day_time = datetime.time(7,0)
        self.night_time = datetime.time(19,0)

        self.day_setting = {
                "hotside_ceil" : 95,
                "hotside_floor" : 90,
                "coolside_ceil" : 85,
                "coolside_floor" : 80,
            }

        self.night_setting = {
                "hotside_ceil" : 75,
                "hotside_floor" : 70,
                "coolside_ceil" : 60,
                "coolside_floor" : 55,
            }

    def set_attribute(self, profile, setting, value):
        if profile == 'day':
            self.day_setting[setting] = value
        elif profile == 'night':
            self.night_setting[setting] = value

    def get_profile(self):
        """Checks if the current time isbetween the two time ranges"""
        current_time = datetime.datetime.now()
        if self.day_time <= datetime.time(current_time.hour, current_time.minute) <= self.night_time:
            return self.day_setting
        else:
            return self.night_setting


class Khalitos_Way(Profile_Setter):

    def __init__(self):
        super().__init__()
        # Initialize data
        self.humidity = 0
        self.temperature = 0

        # Sets pin identifiers to GPIO ints
        GPIO.setmode(GPIO.BCM)
        # Temp sensors
        self.temp_sensor = ada.DHT11
        self.temp1_gpio = 4
        self.temp2_gpio = 22
        # Relays
        self.relay1_gpio = 17
        GPIO.setup(self.relay1_gpio, GPIO.OUT)

        # Set up aiohttp
        self.site = web.Application()
        self.site.add_routes(
            [web.get('/api', self.data_api)]
        )
        # Background the get update tasks
        self.site.on_startup.append(self.start_background_tasks)
        
    def run(self):
        try:
            web.run_app(self.site)
        except KeyboardInterrupt:
            GPIO.cleanup()


    async def data_api(self, request):
        """
        Returns the current data from the sensors
        """
        data = {
            'Humidity': self.humidity,
            'Temperature' : self.temperature
            }
        return web.json_response(data)

    async def sensor_poll(self):
        """Method conducts the data pulls"""
        await asyncio.sleep(3)
        self.humidity, self.temperature = ada.read_retry(self.temp_sensor, self.temp1_gpio)
        self.temperature = self.temperature * 1.8 + 32
        self.invoke_actions()

    def invoke_actions(self):
        profile = self.get_profile()
        current_time = datetime.datetime.now()

        
    async def start_background_tasks(self, site):
        self.site['update_sensor'] = asyncio.create_task(self.sensor_poll())    



Khalitos_Way().run()