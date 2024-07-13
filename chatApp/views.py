from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Room, Message
from todoApp.views import userLogout

@login_required
def createRoom(request):
    if request.method == "POST":
        username = request.user.username
        room = request.POST['room']
        
        try:
            get_room = Room.objects.get(room_name = room)
            
        except Room.DoesNotExist:
            new_room = Room(room_name = room)
            new_room.save()
            
        return redirect('chat-room', room_name = room, username=username)
        
    context = {
        'current_user': request.user
    }
    return render(request, 'chatApp/index.html', context)

def messageView(request, room_name, username):
    get_room = Room.objects.get(room_name = room_name)
    get_messages = Message.objects.filter(room = get_room)
    context = {
        "message": get_messages,
        "user": username,
        "room_name": room_name
    }
    return render(request, 'chatApp/message.html', context)