
from datetime import datetime
from django.db import models
from django import forms


SENSORS = [
    (11, "DHT11"),
    (22, "DHT22")
]

CYCLE = [
    (True, "Daytime"),
    (False, "Night time")
]

CONTROL = [
    ("light", "Lights"),
    ("heat", "Heat Lamp")
]
class DaytimeCycle(models.Model):
    """
    These are the daytime parameters for all the sensors
    """
    daytime_start = models.TimeField(default=datetime.now().time().replace(hour=7, minute=0, second=0),
                                     help_text="HH:MM:SS 24-Hour Format")
    daytime_end = models.TimeField(default=datetime.now().time().replace(hour=19, minute=0, second=0),
                                   help_text="HH:MM:SS 24-Hour Format")

class TemperatureSensor(models.Model):
    """
    The table registers the temperature device along with setting the min max temperature in 
    fahrenheit. The application will use the temperature based on the DaytimeCycle
    """
    device_name = models.CharField(max_length=30, primary_key=True)
    # Day time paremeters
    max_temperature_day = models.FloatField(help_text="Temperature in fahrenheit")
    min_temperature_day = models.FloatField(help_text="Temperature in fahrenheit")
    # Night time paaremters
    max_temperature_night = models.FloatField(help_text="Temperature in fahrenheit")
    min_temperature_night = models.FloatField(help_text="Temperature in fahrenheit")

    sensor_type = models.IntegerField(
        choices=SENSORS,
        default=11,
        help_text="Sensor type to read"
    )
    gpio = models.IntegerField(help_text="GPIO number, not the PIN!", default=-1)

    def __str__(self):
        return self.device_name


class Relay(models.Model):
    relay_name = models.CharField(max_length=30, primary_key=True)
    daytime = models.BooleanField(
        choices=CYCLE,
        default=True,
        help_text="Should this relay power on during the day or night?"
    ) 
    control = models.CharField(
        choices=CONTROL,
        help_text="Will this relay control lights or heat?",
        max_length=30,
        default="light"
    )
    gpio = models.IntegerField(help_text="GPIO number, not the PIN!", default=-1)
    relay_state = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.relay_name} | {self.control}"

class TemperatureRead(models.Model):
    """
    Table updates periodically with the temperature readings. Will also attempt to
    report if the sensor is still communicating incase the sensor gets damaged
    """
    device_name = models.ForeignKey(TemperatureSensor, on_delete=models.CASCADE)
    sample_date = models.DateTimeField(auto_now_add=True)
    
    # Data from sensors
    temperature = models.FloatField()
    humidity = models.FloatField()

    # Able to communicate
    device_online = models.BooleanField()

    def __str__(self):
        return f"{self.device_name}: {self.sample_date}"
