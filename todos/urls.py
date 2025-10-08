from django.urls import path
from todos import views
from todos.views import custom_logout_view, login_view, profile_view

urlpatterns = [
    path('', views.home, name='home'),  # homepage
    path('mark_completed/<int:todo_id>/', views.mark_completed, name='mark_completed'),  # mark a todo as completed
    path('profile/', views.profile_view, name='profile'),  # user profile page
    path('logout/', views.custom_logout_view, name='logout'),  # custom logout
    path('login/', views.login_view, name='login'),  # custom login
    path('edit/<int:id>/', views.edit_todo, name='edit_todo'),  # edit todo by ID
    path('register/', views.register_view, name='register'),  # user registration
    path('tasks/', views.task_list, name='task_list'),  # list of all tasks
    path('tasks/add/', views.add_task, name='add_task'),  # add a new task
]
