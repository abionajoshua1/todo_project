# todos/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo, Categories as Category, Profile
from .forms import TodoForm, UserProfileForm, UserRegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.utils import timezone
from datetime import date
from django.contrib.auth.decorators import login_required

# from django.contrib.auth.decorators import login_required

# @login_required
def home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)  
            todo.user = request.user        
            todo.save()                    
            return redirect('home')
    else:
        form = TodoForm()

    todos = Todo.objects.filter(user=request.user).order_by('-created_at')
    categories = Category.objects.all()  # Assuming you have a Categories model
    return render(request, 'todos/home.html', {'form': form, 'todos': todos,'categories': categories, 'today': date.today()})


def mark_completed(request, todo_id):
    if request.method == 'POST':
        todo = get_object_or_404(Todo, id=todo_id)
        todo.completed = True
        todo.save()
    return redirect('home')

@login_required
def profile_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    todos = Todo.objects.filter(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('profile')
    else:
        form = UserProfileForm(instance=profile)

    context = {
        'form': form,
        'profile': profile,
        'total_tasks': todos.count(),
        'completed_tasks': todos.filter(completed=True).count(),
        'pending_tasks': todos.filter(completed=False).count(),
    }
    return render(request, 'todos/profile.html', context)


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
        user_form = UserRegistrationForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            
            messages.success(request, 'Registration successful. You can now log in.')
            return redirect('login')
        
    else:
        user_form = UserRegistrationForm()
        profile_form = UserProfileForm()
        
    context  = {
    'user_form': user_form, 
    'profile_form': profile_form
    }
        
    return render(request, 'todos/register.html', context)
        
    
def edit_todo(request, id):
    todo = get_object_or_404(Todo, id=id)
    # categories = Category.objects.all()
    if request.method == 'POST':
       form = TodoForm(request.POST, instance=todo)
       if form.is_valid():
           form.save()
           return redirect('home')
       
    return redirect('home')

def task_list(request):
    tasks = Todo.objects.filter(user=request.user).order_by('due_date')
    
    return render(request, 'todos/task_list.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
           new_task = form.save(commit=False)
           new_task.user = request.user  # Associate the task with the logged-in user
           new_task.save()

           return redirect('task_list')  # Redirect to the task list after saving
    else:
        form = TodoForm()
        
    return render(request, 'todos/add_task.html', {'form': form})