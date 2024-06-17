from django.urls import path
from .views import dashboard, update_agent, get_logs

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('update/<int:agent_id>/', update_agent, name='update_agent'),
    path('logs/<int:agent_id>/', get_logs, name='get_logs'),
]
