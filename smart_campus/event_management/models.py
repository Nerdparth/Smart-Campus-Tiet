from django.db import models


class Events(models.Model):
    event_name = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    hosted_by = models.CharField(max_length=200)
    datetime = models.DateTimeField()


class Attendees(models.Model):
    event_name = models.ForeignKey(Events, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    semester = models.CharField(max_length=10)
