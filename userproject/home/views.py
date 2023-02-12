from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import logout,login
from django.contrib.auth.models import User
# Create your views here.
#username:vaibhav
#pass:Vaibhavgarg@12

def index(request):
    if request.user.is_anonymous:
        return redirect("login/")
    return render(request,'index.html')

def loginUser(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username,password)
        #check if user has used correct credential
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("/")    
        else:
            return redirect("login/")

    return render(request,'login.html')

def logoutUser(request):
    logout(request)
    return redirect('login/')