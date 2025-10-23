from django.contrib.auth.models import AbstractUser
from django.db import models 
from datetime import time

def generate_time_choices():
    times = []
    for hour in range(8, 18):
        for minute in (0, 30):
            t = time(hour, minute)
            label = t.strftime("%I:%M %p")
            times.append((t, label))   
    return times

class TA_User(AbstractUser): 
    is_ta = models.BooleanField(default=True)

class TAProfile(models.Model):
    user = models.OneToOneField(TA_User, on_delete=models.CASCADE, related_name="profile")
    courses = models.JSONField(default=list, blank=True)
    description = models.TextField(blank=True)

    COURSE_CHOICES = [
        ("CSCI150", "CSCI258"),
        ("CSCI151", "CSCI332"),
        ("CSCI152", "CSCI340"),
        ("CSCI232", "CSCI272"),
    ]

class AvailabilitySlot(models.Model):
    DAY_CHOICES = [
        (0, "Monday"),
        (1, "Tuesday"),
        (2, "Wednesday"),
        (3, "Thursday"),
        (4, "Friday"),
        (5, "Saturday"),
        (6, "Sunday"),
    ]
    
    TIME_CHOICES = generate_time_choices()
    profile = models.ForeignKey(TAProfile, on_delete=models.CASCADE, related_name="availability_slots")
    day = models.IntegerField(choices=DAY_CHOICES)
    start_time = models.TimeField(choices=TIME_CHOICES)
    end_time = models.TimeField(choices=TIME_CHOICES)
    class Meta:
        ordering = ['day', 'start_time']
    def __str__(self):
        return f"{self.get_day_display()}: {self.start_time.strftime('%I:%M %p')} - {self.end_time.strftime('%I:%M %p')}"