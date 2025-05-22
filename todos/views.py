# todos/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import TodoForm

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

