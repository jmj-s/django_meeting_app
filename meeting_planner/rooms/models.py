from django.db import models

# Create your models here.
from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=200)
    floor = models.IntegerField(default=1)
    room_number = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.name} - {self.floor} - {self.room_number}"
    