import re
from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import todo
from django.contrib.auth.decorators import login_required


# Create your views here.
def loginpage(request):
    
    if request.user.is_authenticated:
        return redirect('todo')
    
    if request.method == 'POST':
        
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        
        valid_user = authenticate(username = username, password = password)
        if valid_user is not None:
            login(request, valid_user)
            return redirect('todo')
        else:
            messages.error(request, 'Incorrect username or password')
            
        
    context = {}
    return render(request, 'todoApp/login.html', context)

def register(request):
    if request.user.is_authenticated:
        return redirect('todo')
    
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        approve = True
        
        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
        regex_num = re.compile('[0-9]')
        regex_upper = re.compile('[A-Z]')
        
        if (len(password) < 8 or regex.search(password) == None or regex_num.search(password) == None or regex_upper.search(password) == None):
            messages.error(request, 'Password must at least contains 8 characters (Including at least 1 special character, 1 number and 1 uppercase letter)')
            approve = False
            
        if (len(username) < 8):
            messages.error(request, 'Username must at least contains 8 characters')
        
        getAllUsers_username = User.objects.filter(username=username)
        if getAllUsers_username: 
            messages.error('Username already exists')
            approve = False
        
        if approve == True:
            new_user = User.objects.create_user(username = username, email = email, password = password)
            new_user.save()
            login(request, new_user)
            return redirect('todo')
    
    context = {}
    return render(request, 'todoApp/register.html', context)

@login_required
def todoPage(request):
    
    if request.method == 'POST':
        content = request.POST.get('content')
        type = request.POST.get('type')
        deadline = request.POST.get('date')
        
        if not deadline:
            deadline = datetime.today().date()

        new_todo = todo(user = request.user, name = content, deadline = deadline, type = type)
        new_todo.save()
        
    
    all_todos = todo.objects.filter(user=request.user)
    context = {
        'current_user': request.user,
        'todos': all_todos
    }
    return render(request, 'todoApp/todo.php', context)

@login_required
def todo_Delete(request, todo_id):
    get_todo = todo.objects.get(user=request.user, id = todo_id)
    get_todo.delete()
    return redirect('todo')

@login_required
def todo_Finished(request, todo_id):
    get_todo = todo.objects.get(user=request.user, id = todo_id)
    get_todo.status = True
    get_todo.save()
    return redirect('todo')

@login_required
def userLogout(request):
    logout(request)
    return redirect('login')
    

    