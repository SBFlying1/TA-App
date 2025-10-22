from django.contrib.auth.models import AbstractUser
from django.db import models 
from datetime import time

def generate_time_choices():
    times = []
    for hour in range(0, 24):
        for minute in (0, 30):
            t = time(hour, minute)
            label = t.strftime("%I:%M %p")
            times.append((t.strftime("%H:%M"), label))
    return times

class TA_User(AbstractUser): 
    is_ta = models.BooleanField(default=True)

class TAProfile(models.Model):
    user = models.OneToOneField(TA_User, on_delete=models.CASCADE, related_name="profile")

    availability_start = models.TimeField(choices=generate_time_choices(), blank=True)
    availability_end = models.TimeField(choices=generate_time_choices(), blank=True)
    description = models.TextField(blank=True)

    courses = models.JSONField(default=list, blank=True)

    COURSE_CHOICES = [
        ("CSCI132", "CSCI 132"),
        ("CSCI232", "CSCI 232"),
        ("CSCI252", "CSCI 252"),
        ("CSCI272", "CSCI 272"),
    ]