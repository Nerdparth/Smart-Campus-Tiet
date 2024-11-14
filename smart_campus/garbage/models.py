from django.db import models

class GarbageSensor(models.Model):
    sensor_id = models.IntegerField(unique=True)
    location = models.CharField(max_length=255)  # Location of the garbage bin
    status = models.CharField(
        max_length=20,
        choices=[('Normal', 'Normal'), ('Overflowed', 'Overflowed')],
        default='Normal'
    )

    def __str__(self):
        return f"Sensor {self.sensor_id} at {self.location} is {self.status}"
