from django.contrib import admin
from .models import GarbageSensor

@admin.register(GarbageSensor)
class GarbageSensorAdmin(admin.ModelAdmin):
    list_display = ('sensor_id', 'location', 'status')
    list_filter = ('status',)
    search_fields = ('sensor_id', 'location')
