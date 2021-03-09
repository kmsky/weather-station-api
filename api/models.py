from django.db import models
from django.utils import timezone


# Create your models here.
class Measurement(models.Model):
    temp = models.FloatField()
    humidity = models.FloatField()
    measure_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "Measurement({}, {}, {}, {})".format(
            self.measure_date.date(),
            self.measure_date.time(),
            self.temp,
            self.humidity
        )
