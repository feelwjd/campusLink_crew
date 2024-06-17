# Create your models here.
from django.db import models


class Agent(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    status = models.TextField()
    log = models.TextField(default='')

    def __str__(self):
        return self.name
