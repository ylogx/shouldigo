from django.db import models

from django.utils import timezone

# Create your models here.

class Weather(models.Model):
    temprature = models.IntegerField(default=0)
    timestamp = models.DateTimeField('Timestamp', default=timezone.now())
    wind = models.IntegerField(default=0)

    #def __init__(self, temprature, timestamp, wind=0):
        #self.temprature = temprature
        #self.timestamp = timestamp
        #self.wind = wind

    def __str__(self):
        output = ''
        output += 'Temprature: ' + str(self.temprature) + ' '
        output += 'Timestamp: ' + str(self.timestamp) + ' '
        output += 'Wind: ' + str(self.wind) + ' '
        return output
