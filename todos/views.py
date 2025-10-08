from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo, Categories as Category, Profile
from .forms import TodoForm, UserProfileForm, UserRegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from datetime import date
from django.contrib.auth.decorators import login_required


def home(request):
    # Require authentication
    if not request.user.is_authenticated:
        return redirect('login')
    
    # Handle new todo submission
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect('home')
    else:
        form = TodoForm()

    # Fetch user todos and categories
    todos = Todo.objects.filter(user=request.user).order_by('-created_at')
    categories = Category.objects.all()
    return render(request, 'todos/home.html', {
        'form': form,
        'todos': todos,
        'categories': categories,
        'today': date.today()
    })


@login_required
def profile_view(request):
    # Get or create profile for logged-in user
    profile, created = Profile.objects.get_or_create(user=request.user)
    todos = Todo.objects.filter(user=request.user)

    # Handle profile update
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
    # Custom login logic
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
    
    return render(request, 'todos/login.html')


def custom_logout_view(request):
    # Log out and redirect to login page
    logout(request)
    return redirect('login')


def register_view(request):
    # User + profile registration
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
        
    return render(request, 'todos/register.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


def task_list(request):
    # Show tasks ordered by due date
    tasks = Todo.objects.filter(user=request.user).order_by('due_date')
    return render(request, 'todos/task_list.html', {'tasks': tasks})


def edit_todo(request, id):
    # Edit an existing todo
    todo = get_object_or_404(Todo, id=id)
    
    if request.method == 'POST':
       form = TodoForm(request.POST, instance=todo)
       if form.is_valid():
           form.save()
           return redirect('home')
    else:
        form = TodoForm(instance=todo)
    
    return redirect('home')


def add_task(request):
    # Add a new todo
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
           new_task = form.save(commit=False)
           new_task.user = request.user
           new_task.save()
           return redirect('task_list')
    else:
        form = TodoForm()
        
    return render(request, 'todos/add_task.html', {'form': form})


def mark_completed(request, todo_id):
    # Mark todo as completed
    if request.method == 'POST':
        todo = get_object_or_404(Todo, id=todo_id)
        todo.completed = True
        todo.save()
    return redirect('home')
