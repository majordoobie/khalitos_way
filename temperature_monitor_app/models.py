
from datetime import datetime
from django.db import models
from django import forms

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

    SENSORS = [
        (11, "DHT11"),
        (22, "DHT22")
    ]
    sensor_type = models.IntegerField(
        choices=SENSORS,
        default=11
    )

    def __str__(self):
        return self.device_name

class LightAccessory(models.Model):
    """
    Table registers the Light sensors along with setting the time of day in EST
    time that they should turn on or off
    """
    device_name = models.CharField(max_length=30, primary_key=True)

    def __str__(self):
        return self.device_name

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

class LightRead(models.Model):
    """
    Same as temperatureRead, but for the lights
    """
    decice_name = models.ForeignKey(LightAccessory, on_delete=models.CASCADE)
    sample_date = models.DateTimeField(auto_now=True)

    # Status of the light
    powered_on = models.BooleanField()

    # Able to communicate
    device_online = models.BooleanField()