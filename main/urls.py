from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('delete/<int:note_id>/', views.delete_note, name='delete_note'),
    path('update/<int:note_id>/', views.update_note, name='update_note'),
    path('show/<int:note_id>/', views.show_note, name='show'),
    path('registration/', views.Registration, name="registration"),
    path('login/', views.LoginView, name='login'),
    path('accounts/login/', views.LoginView, name='login'),
    path('logout/', views.Logout, name="logout"),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
