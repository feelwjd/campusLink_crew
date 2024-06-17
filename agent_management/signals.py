from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Task


@receiver(post_save, sender=Task)
def update_agent_status(sender, instance, **kwargs):
    if instance.status == 'completed':
        instance.assigned_to.status = 'idle'
    elif instance.status == 'in_progress':
        instance.assigned_to.status = 'busy'
    instance.assigned_to.save()
