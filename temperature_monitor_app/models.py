from django.db import models

# Sensor registration with settings
class TemperatureSensors(models.Model):
    # Alias name as the primary key
    device_name = models.CharField(max_length=30, primary_key=True)

    # Parameters
    max_temperature = models.FloatField()
    min_temperature = models.FloatField()

class LightSensors(models.Model):
    device_name = models.CharField(max_length=30, primary_key=True)

    # Parameters
    turn_on_start = models.DateField()
    turn_on_end = models.DateField()

# History data of sensor statuses
class TemperatureRead(models.Model):
    # Alias name of the temperature reader with cascade
    device_name = models.ForeignKey(TemperatureSensors, on_delete=models.CASCADE)
    
    # Timestamp when the record is created
    sample_date = models.DateField(auto_now=True)
    
    # Data from sensors
    temperature = models.FloatField()
    humidity = models.FloatField()

    # Able to communicate
    device_online = models.BooleanField()

class LightRead(models.Model):
    # Alias name of the temperature reader
    decice_name = models.ForeignKey(LightSensors, on_delete=models.CASCADE)
    
    # Timestamp when the record is created
    sample_date = models.DateField(auto_now=True)

    # Status of the light
    powered_on = models.BooleanField()

    # Able to communicate
    device_online = models.BooleanField()
