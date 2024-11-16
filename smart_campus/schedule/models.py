from django.db import models

# Constants for the days of the week and times
DAYS_OF_WEEK = [
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
]

SUBJECTS = [
    ('Maths', 'Maths'),
    ('Data Structures', 'Data Structures'),
    ('Web Technology', 'Web Technology'),
    ('Automata Theory', 'Automata Theory'),
    ('Digital Design', 'Digital Design'),
]

TIMINGS = [
    ('9:00-10:00', '9:00-10:00'),
    ('10:00-11:00', '10:00-11:00'),
    ('11:00-12:00', '11:00-12:00'),
    ('12:00-1:00', '12:00-1:00'),
    ('2:00-3:00', '2:00-3:00'),
]

class Schedule(models.Model):
    day = models.CharField(max_length=10, choices=DAYS_OF_WEEK)
    time = models.CharField(max_length=20, choices=TIMINGS)
    subject = models.CharField(max_length=50, choices=SUBJECTS)

    class Meta:
        unique_together = ('day', 'time')  # Ensure no duplicate day/time combinations

    def __str__(self):
        return f"{self.day} {self.time}: {self.subject}"
