from django.db import models


class bookingsystem(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.IntegerField(default=1, max_length=30)
    to = models.CharField(max_length=30)
    departuredate = models.CharField(default=1, max_length=30)
    returntrip = models.CharField(default=1, max_length=30)


def __str__(self):
    return self.name
