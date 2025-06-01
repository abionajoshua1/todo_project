from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    title = models.CharField(max_length=200)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    due_date = models.DateField(null=True, blank=True)
    categories = models.ForeignKey('Categories', on_delete=models.SET_NULL, related_name='todos', null=True, blank=True)
    
    def is_overdue(self):
        return self.due_date and self.due_date < timezone.now().date()
    

    def __str__(self):
        return self.title
    
# class User(models.Model):
#     pass

class Categories(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
