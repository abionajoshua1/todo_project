from django.contrib import admin
from .models import Todo, Categories


class TodoAdmin(admin.ModelAdmin):
    # Fields to display in the admin list view
    list_display = ('title', 'user', 'completed', 'due_date', 'user_email', 'categories')
    
    # Custom column to show user email
    def user_email(self, obj):
        return obj.user.email
    user_email.short_description = 'Email'
    
    # Sidebar filters
    list_filter = ('user', 'completed', 'categories')
    
    # Search functionality
    search_fields = ('title',)
    
    # Default ordering
    ordering = ('user',)


# Register models in the admin site
admin.site.register(Todo, TodoAdmin)
admin.site.register(Categories)
