from django.urls import path
from .consumers import chatConsumer

websocket_urlpatterns = [
    path('ws/notification/<str:room_name>/', chatConsumer.as_asgi()),
]