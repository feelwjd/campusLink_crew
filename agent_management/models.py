# Create your models here.
from django.db import models


class Agent(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    status = models.TextField()
    log = models.TextField(default='')
    

class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    assigned_to = models.ForeignKey(Agent, on_delete=models.CASCADE, related_name='tasks')
    status = models.CharField(max_length=50, default='pending')
    result = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
