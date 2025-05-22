from django.urls import path
from todos import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('mark_completed/<int:todo_id>/', views.mark_completed, name='mark_completed'),
    path('profile/', views.profile_view, name='profile'), 
    path('logout/', auth_views.LogoutView.as_view(template_name='todos/logout.html'), name='logout'),
]
