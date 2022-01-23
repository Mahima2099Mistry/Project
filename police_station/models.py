from django.db import models

# Create your models here.
class Police_station(models.Model):
    police_station_name = models.CharField(max_length=50)
    area = models.TextField()

    def __str__(self):
        return self.police_station_name