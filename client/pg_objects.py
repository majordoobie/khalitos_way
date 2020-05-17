from datetime import datetime
class TemperatureSensor:
    def __init__(self, device_name, high_day, low_day, high_night, low_night, sensor_type, gpio):
        self.device_name = device_name 
        self.high_day = high_day
        self.low_day = low_day
        self.high_night = high_night
        self.low_night = low_night
        self.sensor_type = sensor_type
        self.gpio = gpio

        self.temperature = 0
        self.humidity = 0
        self.device_online = False

    def __str__(self):
        return self.device_name

class DaytimeCycle:
    def __init__(self, morning, night):
        self.morning = morning
        self.night = night
        self.daytime = self.get_cycle()

    def get_cycle(self):
        now = datetime.now().time()
        if now > self.morning and now < self.night:
            return True
        else:
            return False

class Relay:
    def __init__(self, relay_name, daytime, gpio, relay_state, control):
        self.relay_name = relay_name
        self.daytime = daytime
        self.gpio = gpio
        self.control = control
        self.relay_state = relay_state
    
    def __str__(self):
        return f"{self.relay_name} | {self.control} | {self.relay_state}"