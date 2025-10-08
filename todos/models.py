from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.conf import settings    


# ---------------------------
# Todo Model
# ---------------------------
class Todo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)  # linked to user
    title = models.CharField(max_length=200)  # task title
    description = models.TextField()  # task description
    completed = models.BooleanField(default=False)  # completion status
    created_at = models.DateTimeField(auto_now_add=True)  # set once on creation
    updated_at = models.DateTimeField(auto_now=True)  # auto-updated on save
    due_date = models.DateField(null=True, blank=True)  # optional due date
    categories = models.ForeignKey('Categories', on_delete=models.SET_NULL, related_name='todos', null=True, blank=True)  # optional category
    
    def is_overdue(self):
        return self.due_date and self.due_date < timezone.now().date()  # check if task is overdue

    def __str__(self):
        return self.title


# ---------------------------
# Categories Model
# ---------------------------
class Categories(models.Model):
    name = models.CharField(max_length=100)  # category name
    
    def __str__(self):
        return self.name


# ---------------------------
# Profile Model
# ---------------------------
class Profile(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
        ('prefer_not_to_say', 'Prefer not to say'),
    ]
    
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)  # one profile per user
    first_name = models.CharField(max_length=30, default='First')
    last_name = models.CharField(max_length=30, default='Last')
    created_at = models.DateTimeField(default=timezone.now)  # profile creation timestamp
    updated_at = models.DateTimeField(auto_now=True)  # profile update timestamp
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_initial(self):
        return f'{self.first_name[0].upper()}{self.last_name[0].upper()}'  # initials from name


# ---------------------------
# Custom User Model
# ---------------------------
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)  # enforce unique email
    
    def __str__(self):
        return self.username
