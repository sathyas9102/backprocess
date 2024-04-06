import email
from telnetlib import AUTHENTICATION
from unittest import result
from django.shortcuts import render,redirect
from . models import register
from . import views
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
# from django.contrib.auth import authenticate,login,auth 
from .models import register
from django.contrib.auth import login,authenticate



# Create your views here.


def home(request):
    return render(request,"home.html")

def story(request):
    return render(request,"story.html")

def product(request):
    return render(request,"product.html")

# def select(request):
#     return render(request,"select.html")

def milk(request):
    return render(request,"milk.html")

def bread(request):
    return render(request,"bread.html")

def eggs(request):
    return render(request,"eggs.html")

def protein(request):
    return render(request,"protein.html")

def white_egg(request):
    return render(request,"white_egg.html")

def a2_cow(request):
    return render(request,"a2_cow.html")

def buffalo_milk(request):
    return render(request,"buffalo_milk.html")

def coconut(request):
    return render(request,"coconut.html")

def cow_milk(request):
    return render(request,"cow_milk.html")

def login(request):
    
    if request.method=='POST':
        Email=request.POST['email']
        password=request.POST['password']

        user=authenticate(Email=email,password=password)
        
        if user is not None:
            login(request,user)
            fname=user.first_name
            return render(request,"home.html",{'fname':fname})
        
        else:
            messages.error(request,"bad credentials")
            return redirect('home')
    else:
        return render(request,"login.html")

def register(request):
    
    if request.method=="POST":
        username=request.POST('username')
        f_name=request.POST('fname')
        l_name=request.POST('lname')
        email=request.POST('email')
        password=request.POST('password')
        # pass2=request.POST('pass2')
        
        user=User.objects.create_user(username,f_name,l_name,email,password)
        # user.First_name=fname
        # user.Last_name=lname
        
        user.save()
        
        messages.success(request,"you are registered")
        
        return redirect('login')
    else:  
        return render(request,"register.html",{})


        
        
#         user=user.object.create_user(First_Name=First_Name,Last_Name=Last_Name,email=email,password=password,)   

#        user.save()
#        print('user created')
#        return redirect('/')
#    else:
#        return render(request,'register.html')