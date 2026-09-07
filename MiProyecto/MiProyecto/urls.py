"""
URL configuration for MiProyecto project.
"""
from django.contrib import admin
from django.urls import path
from App2 import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
]
