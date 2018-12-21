"""bankinfo URL Configuration

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

from prasad import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.showindex),
    path('head/', views.head),
    path('body/', views.body),

    path('open/', views.open),
    path('accountopen/', views.accountopen),
    path('accountdetails/', views.accountdetails),
    path('accountcsvfile/', views.accountcsvfile),

    path('manager/', views.manager),
    path('managerdetails/', views.managerdetails),

    path('depo/', views.depo),
    path('deposite/', views.deposite1),
    path('depositedetails/', views.depositedetails),
    path('depositeCSVfile/', views.depositeCSVfile),


    path('withdrawlogin/', views.withdrawlogin),
    path('withdrawlogindeails/', views.withdrawlogindetails),
    path('withdrawdetails/', views.withdrawdetails),





]
