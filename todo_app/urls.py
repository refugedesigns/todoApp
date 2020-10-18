from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='home'),
    path('update_todo/<str:pk>/', views.update_todo, name='update_todo'),
    path('mark_completed/<str:pk>/', views.mark_completed, name='mark_completed'),
    path('unmark/<str:pk>/', views.unmark, name='unmark'),
    path('delete_todo/<str:pk>/', views.delete_todo, name='delete_todo'),
]
