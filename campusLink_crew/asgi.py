import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from agent_management.consumers import AgentConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'campusLink_crew.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(
        URLRouter([
            path('ws/agent_management/', AgentConsumer.as_asgi()),
        ])
    ),
})
