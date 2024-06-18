from django.db import models


class Agent(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    goal = models.TextField()
    status = models.CharField(max_length=50, default='idle')
    backstory = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    description = models.TextField()
    assigned_to = models.ForeignKey(Agent, on_delete=models.CASCADE, related_name='tasks', null=True, blank=True)
    status = models.CharField(max_length=50, default='pending')
    result = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.description
