"""dummy4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from app4 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('head/', views.head),
    path('menu/', views.menu),
    path('body/', views.body),
    path('register/', views.student_register),
    path('registerdetails/', views.student_registerdetails),
    path('student_login/', views.student_login),
    path('student_logindetails/', views.student_logindetails),
    path('faculity_register/', views.faculity_register),
    path('faculity_registeration/', views.faculity_registeration),
    path('faculity_login/', views.faculity_login),
    path('faculity_logindetails/', views.faculity_logindetails),
]
