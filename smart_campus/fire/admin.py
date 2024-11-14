from django.contrib import admin
from .models import FireSensor

@admin.register(FireSensor)
class FireSensorAdmin(admin.ModelAdmin):
    list_display = ('sensor_id', 'location')
