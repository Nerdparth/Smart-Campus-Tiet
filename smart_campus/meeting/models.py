from django.db import models

class Meeting(models.Model):
    url = models.URLField(max_length=500)  # Field to store the meeting URL

    def __str__(self):
        return self.url
