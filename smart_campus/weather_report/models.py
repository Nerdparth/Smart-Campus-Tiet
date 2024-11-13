# weather_report/models.py
from django.db import models


class SensorData(models.Model):
    air_quality = models.IntegerField()
    air_humidity = models.FloatField()
    temperature = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"SensorData at {self.timestamp}"
