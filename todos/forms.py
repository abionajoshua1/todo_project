from django import forms
from .models import Todo
from .models import Profile
from django.contrib.auth import get_user_model

User = get_user_model()

from django.contrib.auth.forms import UserCreationForm


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'due_date', 'categories'] 
        exclude = ['user']
        #'completed'
        
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
        }
        
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'gender', 'date_of_birth'] #'bio', ,  'avatar'
        
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            # 'bio': forms.Textarea(attrs={'rows': 3}),
        }


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']