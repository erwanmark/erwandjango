from django.db import models


class people(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.IntegerField(default=1, max_length=30)
    country = models.CharField(default=1, max_length=30)
    city = models.CharField(default=1, max_length=30)
    age = models.IntegerField()
    gender = models.CharField(max_length=30)


def __str__(self):
    return self.name
