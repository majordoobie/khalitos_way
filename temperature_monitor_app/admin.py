from django.contrib import admin
from .models import TemperatureRead, TemperatureSensors, LightRead, LightSensors

admin.site.register(TemperatureRead)
admin.site.register(TemperatureSensors)
admin.site.register(LightRead)
admin.site.register(LightSensors)