"""
ASGI config for minigames project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.management import call_command

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'minigames.settings')

from django import setup
setup()

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter

from games_queue.routing import websocket_urlpatterns

call_command('makemigrations')
call_command('migrate')

asgi_application = get_asgi_application()

application = ProtocolTypeRouter({
            "http": asgi_application,
            "websocket": URLRouter(websocket_urlpatterns)
                       })
