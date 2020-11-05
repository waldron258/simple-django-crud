from django.db import models

# Create your models here.

class Car(models.Model):
    owner = models.CharField(max_length=100)
    plate = models.CharField(max_length=10, unique=True)
    carModel = models.CharField(max_length=100)
    year = models.IntegerField()