from django.contrib import admin
from .models import TemperatureSensor, Relay, DaytimeCycle

class TemperatureSensorAdmin(admin.ModelAdmin):
    # List out the things you want to show in the admin page
    list_display = (
        'device_name',
        'max_temperature_day',
        'min_temperature_day',
        'max_temperature_night',
        'min_temperature_night',
        'sensor_type',
        'gpio'
    )

class RelayAdmin(admin.ModelAdmin):
    list_display = (
        'relay_name',
        'daytime',
        'control',
        'gpio',
        'relay_state'
    )
class DaytimeCycleAdmin(admin.ModelAdmin):
    list_display = (
        'daytime_start',
        'daytime_end'
    )

admin.site.register(DaytimeCycle, DaytimeCycleAdmin)
admin.site.register(TemperatureSensor, TemperatureSensorAdmin)
admin.site.register(Relay, RelayAdmin)
