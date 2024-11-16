from django.db import models

class Announcement(models.Model):
    content = models.TextField()  

    def __str__(self):
        return f"Announcement: {self.content[:50]}..."  
