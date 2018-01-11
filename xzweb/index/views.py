from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# 首页
def index(request):
    return render(request, 'index.html')
#登录页面
def page_login(request):
    return render(request, 'page_login.html')
#注册页面
def page_registration(request):
    return render(request, 'page_registration.html')