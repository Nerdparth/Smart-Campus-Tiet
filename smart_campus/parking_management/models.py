from django.db import models


class ParkingData(models.Model):
    sensor_id = models.IntegerField()
    sensor_location = models.CharField(max_length=300)
    parking_status = models.BooleanField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"SensorData at {self.timestamp}"
