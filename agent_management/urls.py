from django.urls import path
from .views import dashboard, assign_task, update_task

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('assign/<int:agent_id>/', assign_task, name='assign_task'),
    path('update/<int:task_id>/', update_task, name='update_task'),
]
