from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginpage, name ="login"),
    path('register/', views.register, name='register'),
    path('Logout/', views.userLogout, name='logout'),
    path('todo/', views.todoPage, name='todo'),
    path('delete-todo/<str:todo_id>', views.todo_Delete, name="delete-todo"),
    path('Finished-todo/<str:todo_id>', views.todo_Finished, name='Finished-todo')
]