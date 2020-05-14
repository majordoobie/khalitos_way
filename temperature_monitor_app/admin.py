from django.contrib import admin
from .models import TemperatureSensor, LightAccessory

class TemperatureSensorsAdmin(admin.ModelAdmin):
    # List out the things you want to show in the admin page
    list_display = (
        'device_name',
        'max_temperature_day',
        'min_temperature_day',
        'max_temperature_night',
        'min_temperature_night'
    )

class LightSensorsAdmin(admin.ModelAdmin):
    list_display = (
        'device_name',
    )


admin.site.register(TemperatureSensor, TemperatureSensorsAdmin)
admin.site.register(LightAccessory, LightSensorsAdmin)
