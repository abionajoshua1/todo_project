# todos/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import TodoForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.utils import timezone
from datetime import date


def home(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TodoForm()

    todos = Todo.objects.all().order_by('-created_at')
    return render(request, 'todos/home.html', {'form': form, 'todos': todos, 'today': date.today()})

def mark_completed(request, todo_id):
    if request.method == 'POST':
        todo = get_object_or_404(Todo, id=todo_id)
        todo.completed = True
        todo.save()
    return redirect('home')
    
def profile_view(request):
    return render(request, 'profile.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # change to your actual home route
        else:
            messages.error(request, 'Invalid username or password')
    
    return render(request, 'todos/login.html')

def custom_logout_view(request):
    logout(request)
    # return render(request, 'todos/logout.html')
    return redirect('login')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful. You can now log in.')
            return redirect('login')
        else:     
            return render(request, 'todos/register.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'todos/register.html', {'form': form})
    

def edit_todo(request, id):
    todo = get_object_or_404(Todo, id=id)
    if request.method == 'POST':
       form = TodoForm(request.POST, instance=todo)
       if form.is_valid():
           form.save()
           return redirect('home')
       
    return redirect('home')