"""
URL configuration for app_1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from app_2 import views
from app_2.views import register

import app_2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('home.html',views.home),
    path('story.html',views.story),
    path('product.html',views.product),
    path('milk.html',views.milk),
    path('bread.html',views.bread),
    path('eggs.html',views.eggs),
    path('protein.html',views.protein),
    path('white_egg.html',views.white_egg),
    path('buffalo_milk',views.buffalo_milk),
    path('coconut.html',views.coconut),
    path('cow_milk.html',views.cow_milk),
    path('a2_cow.html',views.a2_cow),
    path('login.html',views.login,name="login"),
    path('register.html/',views.register,name="register"),
     # path('register/', register.as_view(), name='register'),
]
