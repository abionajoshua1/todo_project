# todos/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import TodoForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TodoForm()

    todos = Todo.objects.all().order_by('-created_at')
    return render(request, 'todos/home.html', {'form': form, 'todos': todos})

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
    if request.method == 'POST':
        logout(request)
        return render(request, 'todos/logout.html')  # render your logged out page
    else:
        return redirect('home')