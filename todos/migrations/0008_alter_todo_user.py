from django.db import migrations

def assign_default_user(apps, schema_editor):
    Todo = apps.get_model('todos', 'Todo')
    User = apps.get_model('auth', 'User')
    
    default_user = User.objects.get(pk=1)  # Make sure user with ID 1 exists

    for todo in Todo.objects.filter(user__isnull=True):
        todo.user = default_user
        todo.save()

class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0007_todo_user'),
    ]

    operations = [
        migrations.RunPython(assign_default_user),
    ]
