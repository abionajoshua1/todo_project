from django import forms
from .models import Todo
from django.contrib.auth.models import User


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'due_date', 'categories'] #'completed'
        
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
        }
        
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']