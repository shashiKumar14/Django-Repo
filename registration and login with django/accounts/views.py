# from audioop import reverse
# from django.shortcuts import render,redirect
# from django.contrib.auth.models import User

from django.shortcuts import render,redirect
import requests
# from bs4 import BeautifulSoup
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from accounts.models import Useradd,Contact
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def bike(request):
    return render(request,"index.html")
def home(request):
    return render(request,'index.html')

# def register(request):
#     if request.method=='POST':
#         username=request.POST.get("username")
#         password=request.POST.get("password")
#         email=request.POST.get("email")

#         user=User.objects.create_user(username,email,password)
#         user.save()
#         return redirect('home')
#     return render(request,'register.html')

# Create your views here.
def login_user(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user= authenticate(username=username, password=password)
        if user is not None:

            login(request,user)
        
        return redirect("home")

    return render(request,"login.html")
def register(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        email=request.POST.get("email")
        c = User.objects.create_user(username=username,email=email,password=password)
        c.save()
        return redirect("login")
    
    return render(request,"register.html")

def logout_user(request):
    logout(request)
    return redirect("login")

def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        message=request.POST['message']
        


        c=Contact(name=name,email=email,message=message)
        c.save()
        return redirect("home")

    return render(request,"contact.html")