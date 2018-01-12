from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.models import User

from django.contrib import auth

from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

# 首页
def index(request):
    return render(request, 'index.html')
#登录页面
def page_login(request):
    return render(request, 'page_login.html')
#注册页面
def page_registration(request):
    return render(request, 'page_registration.html')
