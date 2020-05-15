class TemperatureSensor:
    def __init__(self, sensor, high_day, low_day, high_night, low_night):
        self.sensor = sensor
        self.high_day = high_day
        self.low_day = low_day
        self.high_night = high_night
        self.low_night = low_night


class Lighting:
    def __init__(self, lamp):
        self.lamp = lamp

class DaytimeCycle:
    def __init__(self, morning, night):
        self.morning = morning
        self.night = night