from django.contrib import admin
from .models import Todo, Categories

class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'completed', 'due_date', 'user_email', 'categories')
    
    def user_email(self, obj):
        return obj.user.email
    user_email.short_description = 'Email'
    
    list_filter = ('user', 'completed', 'categories')
    search_fields = ('title',)
    ordering = ('user',)

admin.site.register(Todo, TodoAdmin)
admin.site.register(Categories)