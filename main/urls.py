from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('delete/<int:note_id>/', views.delete_note, name='delete_note'),
    path('update/<int:note_id>/', views.update_note, name='update_note'),
    path('show/<int:note_id>/', views.show_note, name='show'),
]
