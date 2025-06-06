from django.urls import path
from todos import views
# from django.contrib.auth import views as auth_views
from  todos.views import custom_logout_view, login_view, profile_view

urlpatterns = [
    path('', views.home, name='home'),
    path('mark_completed/<int:todo_id>/', views.mark_completed, name='mark_completed'),
    path('profile/', views.profile_view, name='profile'), 
    path('logout/',views.custom_logout_view,  name='logout'),
    path('login/', views.login_view, name='login'),
    path('edit/<int:id>/', views.edit_todo, name='edit_todo'),
    path('register/', views.register_view, name='register'),
    path('tasks/', views.task_list, name='task_list'),
    path('tasks/add/', views.add_task, name='add_task'),

]
