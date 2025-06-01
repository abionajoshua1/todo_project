from django.db import migrations

def assign_default_user(apps, schema_editor):
    Todo = apps.get_model('todos', 'Todo')
    User = apps.get_model('auth', 'User')
    
    # Make sure a user with ID=1 exists before running this
    default_user = User.objects.get(pk=1)

    for todo in Todo.objects.filter(user__isnull=True):
        todo.user = default_user
        todo.save()

class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0008_alter_todo_user'),  # Replace with your actual previous migration file name
    ]

    operations = [
        migrations.RunPython(assign_default_user),
    ]
