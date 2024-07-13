from django.urls import path
from . import views

urlpatterns = [
    path('room-create/', views.createRoom, name='room-create'),
    path('<str:room_name>/<str:username>/', views.messageView, name='chat-room')
]