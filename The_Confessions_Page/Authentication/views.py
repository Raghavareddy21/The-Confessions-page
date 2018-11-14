from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from . import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
# Create your views here.
def signup(request):
    if request.user.is_authenticated:
        return HttpResponse("You have already logged in :)")
    else:
        if request.method=='POST':
            form=forms.Registration(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponse("You have successfully signed up for the Confessions page.")
            else:
                return render(request,'Authentication/signup.html',{'form':form})
        else:
            form= forms.Registration()
        return render(request,'Authentication/signup.html',{'form':form})
def user_login(request):
    if request.user.is_authenticated:
        return HttpResponse("You have already logged in :)")
    else:
        if request.method=='POST':
            username=request.POST['username']
            password=request.POST['password']
            user=authenticate(username=username,password=password)
            member=User.objects.get(username=request.POST['username'])
            if user is not None:
                if user.is_active:
                    request.session['User_id']=member.id
                    login(request, user)
                    return redirect('/Confession/Home/')
                else:
                    return render(request,'Authentication/login.html',{'err':'Your account is not active at the moment please contact the Administration'})
            else:
                return render(request,'Authentication/login.html',{'err':'Please enter your Authenticated credentials'})
        else:
            return render(request,'Authentication/login.html',{'err':''})
def user_logout(request):
    if not request.user.is_authenticated:
        return HttpResponse("You have already logged out :)")
    else:
        logout(request)
        return HttpResponse("You have successfully logged out :)")
