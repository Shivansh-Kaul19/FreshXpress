from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
# Create your views here.

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('pass')
        my_user=User.objects.create_user(uname,email,password)
        my_user.save()
        return redirect('login')
    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        email1=request.POST.get('email')
        pass1=request.POST.get('pass')
        user=authenticate(request,email=email1,password=pass1)
        if user is not None:
             login(request,user)
        else:
            return HttpResponse("Email or Password is incorrect!!")

    return render (request,'login.html')