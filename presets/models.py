# presets/models.py
from django.db import models

class Preset(models.Model):
    name = models.CharField(max_length=100)
    numberOfKeys = models.IntegerField()
    lowerKey = models.IntegerField()
    modulationIndex = models.FloatField()
    harmonicity = models.FloatField()

    def __str__(self):
        return self.name

# Create your models here.
