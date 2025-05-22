from django.urls import path
from todos import views

urlpatterns = [
    path('', views.home, name='home'),
     path('mark_completed/<int:todo_id>/', views.mark_completed, name='mark_completed'),
]
