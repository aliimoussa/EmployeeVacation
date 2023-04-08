from django.http import *
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import get_user_model
from django.contrib.auth import login, logout,get_user_model,authenticate
from .models import Account
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.db import IntegrityError
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import json

from django.http import JsonResponse
# Create your views here.



def index(request):
    return redirect('home')

@login_required(login_url='login')
def home(request):
    return redirect('vacation-user')
    #return render(request,'home.html')

def register_view(request):
    if request.method == 'POST':
        #print(request.POST)
        try:
            obj,created = Account.objects.update_or_create(
                first_name=request.POST['firstname'],
                last_name=request.POST['lastname'],
                username=request.POST['firstname'],
                email=request.POST['email'],
                password=make_password(request.POST['password']))
            obj=authenticate(email=email,password=password)
            login(request, obj)
            return redirect('login')
                
        except IntegrityError:
            return redirect('login')
    return render(request, 'accounts/register.html')

def login_view(request):
    next_page=request.GET.get('next', '/')
    if request.user.is_authenticated:
        return redirect(next_page)
    if request.method == 'POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=email)
        except UserModel.DoesNotExist:
            user = None
        else:
            if user.check_password(password):
                user = user
            else:
                user=None
        if user is not None and user.is_active:
            login(request, user)
            return redirect(next_page)
        else:
            messages.info(request,'Email or password is incorrect!')
    return render(request, 'accounts/login.html')

@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def accounts(request):
    accounts=Account.objects.all()
    return render(request,'home.html',{'accounts':accounts})


