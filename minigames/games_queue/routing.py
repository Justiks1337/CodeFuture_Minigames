from .consumers import PlayerWebsocket
from django.urls import path, re_path, utils


websocket_urlpatterns = [
    path('websockets/queue/<str:tag>/', PlayerWebsocket.as_asgi())
]