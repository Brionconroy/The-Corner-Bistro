from django.db import models
from django.contrib.auth.models import User


class Reservation(models.Model):
    naming_id = models.IntegerField(primary_key=True)
    date_and_time = models.DateTimeField()
    duration = models.DurationField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-naming_id"]