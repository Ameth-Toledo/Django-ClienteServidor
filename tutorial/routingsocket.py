#aqui van todas las ruta para websockets
from django.urls import path
from .consumers import MyConsumer

websocket_urlpatterns = [
    path('ws/somepath/', MyConsumer.as_asgi()),
]