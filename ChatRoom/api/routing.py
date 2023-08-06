from django.urls import path 
from . import consumers


websocket_urlpatterns = [
    path('ws/sc/<str:groupname>/', consumers.MyJsonWebsocketConsumer.as_asgi()),
    path('ws/ac/',consumers.MyAsyncConsumer.as_asgi()),
]