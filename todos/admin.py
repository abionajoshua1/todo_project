from django.contrib import admin
from .models import Todo, Categories

class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'completed')

admin.site.register(Todo, TodoAdmin)
admin.site.register(Categories)