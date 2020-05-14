from django.contrib import admin
from .models import TemperatureSensor, LightAccessory, DaytimeCycle

class TemperatureSensorAdmin(admin.ModelAdmin):
    # List out the things you want to show in the admin page
    list_display = (
        'device_name',
        'max_temperature_day',
        'min_temperature_day',
        'max_temperature_night',
        'min_temperature_night'
    )

class LightAccessoryAdmin(admin.ModelAdmin):
    list_display = (
        'device_name',
    )

class DaytimeCycleAdmin(admin.ModelAdmin):
    list_display = (
        'daytime_start',
        'daytime_end'
    )

admin.site.register(DaytimeCycle, DaytimeCycleAdmin)
admin.site.register(TemperatureSensor, TemperatureSensorAdmin)
admin.site.register(LightAccessory, LightAccessoryAdmin)
