from django.db import models

class FireSensor(models.Model):
    sensor_id = models.IntegerField(unique=True)
    location = models.CharField(max_length=255)  # Location of the fire sensor

    def __str__(self):
        return f"Sensor {self.sensor_id} at {self.location}"
