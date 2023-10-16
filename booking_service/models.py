from django.db import models
from django.contrib.auth.models import User


class Reservation(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    naming_id = models.IntegerField(primary_key=True)
    date_and_time = models.DateTimeField()
    num_guests = models.PositiveSmallIntegerField()

    class Meta:
        ordering = ["naming_id"]
        