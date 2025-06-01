from django.db import migrations

def fix_null_users(apps, schema_editor):
    Todo = apps.get_model('todos', 'Todo')
    # For example, assign a default user ID (replace 1 with an actual valid user id)
    default_user_id = 1
    todos_with_null_user = Todo.objects.filter(user__isnull=True)
    for todo in todos_with_null_user:
        todo.user_id = default_user_id
        todo.save()

class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0011_alter_todo_user'),
    ]

    operations = [
        migrations.RunPython(fix_null_users),
    ]
