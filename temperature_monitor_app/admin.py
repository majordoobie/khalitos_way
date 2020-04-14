from django.contrib import admin
from .models import TemperatureSensors, LightSensors

class TemperatureSensorsAdmin(admin.ModelAdmin):
    # List out the things you want to show in the admin page
    list_display = (
        'device_name', 'max_temperature', 'min_temperature'
    )

class LightSensorsAdmin(admin.ModelAdmin):
    list_display = (
        'device_name', 'turn_on_start', 'turn_on_end'
    )


admin.site.register(TemperatureSensors, TemperatureSensorsAdmin)
admin.site.register(LightSensors, LightSensorsAdmin)
