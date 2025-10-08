# Import Django forms base class
from django import forms

# Import your app models (Todo and Profile) to build forms around them
from .models import Todo
from .models import Profile

# Get the custom user model (in case you're using AbstractUser / AbstractBaseUser)
from django.contrib.auth import get_user_model
User = get_user_model()

# Import Django's built-in UserCreationForm (handles user registration logic)
from django.contrib.auth.forms import UserCreationForm


# ---------------------------
# Form for Todo Model
# ---------------------------
class TodoForm(forms.ModelForm):
    """
    Form to create and update Todo objects.
    Inherits from Django's ModelForm so fields are automatically tied to the model.
    """
    class Meta:
        # Use the Todo model as the base
        model = Todo

        # Explicitly specify which fields should appear in the form
        fields = ['title', 'description', 'due_date', 'categories']

        # Exclude certain fields you don’t want users to modify manually
        # For example, 'user' should usually be set in the backend (views) not by the user
        exclude = ['user']  

        # Add custom widgets to improve form rendering
        widgets = {
            # Display due_date as an HTML <input type="date">
            'due_date': forms.DateInput(attrs={'type': 'date'}),
        }
        # Note: 'completed' field is commented out; likely handled in code or admin


# ---------------------------
# Form for Profile Model
# ---------------------------
class UserProfileForm(forms.ModelForm):
    """
    Form for editing user profile details (linked to Profile model).
    """
    class Meta:
        # Use the Profile model
        model = Profile

        # List of fields that should be editable via this form
        fields = ['first_name', 'last_name', 'gender', 'date_of_birth']  
        # 'bio' and 'avatar' are commented out — they can be enabled if needed

        # Custom widgets for specific fields
        widgets = {
            # Render date_of_birth as an HTML <input type="date">
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),

            # Example if bio was included:
            # 'bio': forms.Textarea(attrs={'rows': 3}),
        }


# ---------------------------
# User Registration Form
# ---------------------------
class UserRegistrationForm(UserCreationForm):
    """
    Custom registration form that extends Django's built-in UserCreationForm.
    Adds 'email' field to the standard username + password fields.
    """
    class Meta:
        # Use the custom user model (works even if you've overridden User)
        model = User

        # Fields shown during registration
        fields = ['username', 'email', 'password1', 'password2']
