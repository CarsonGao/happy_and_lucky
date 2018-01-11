from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from index.models import User
from index.forms import UserForm

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect

# 首页
def index(request):
    return render(request, 'index.html')
#登录页面
def page_login(request):
    return render(request, 'page_login.html')
#注册页面
def page_registration(request):
    return render(request, 'page_registration.html')


#注册
@csrf_exempt
def register_view(req):
    context = {}
    if req.method == 'POST':
        form = UserForm(req.POST)
        if form.is_valid():
            #获得表单数据
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            #添加到数据库（还可以加一些字段的处理）
            User.objects.create(username=username, password=password)
            #添加到session
            req.session['username'] = username
            #重定向到首页
            return HttpResponseRedirect('/')
    else:
        context = {'isLogin':False}
    #将req 、页面 、以及context{}（要传入html文件中的内容包含在字典里）返回
    return  render(req,'register.html',context)

#登陆
@csrf_exempt
def login_view(req):
    context = {}
    if req.method == 'POST':
        form = UserForm(req.POST)
        if form.is_valid():
            #获取表单用户密码
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            #获取的表单数据与数据库进行比较
            user = User.objects.filter(username = username,password = password)
            if user:
                #比较成功，跳转index
                req.session['username'] = username
                return HttpResponseRedirect('/')
            else:
                #比较失败，还在login
                context = {'isLogin': False,'pawd':False}
                return render(req, 'login.html', context)
    else:
        context = {'isLogin': False,'pswd':True}
    return render(req, 'login.html', context)

#登出
def logout_view(req):
    #清理cookie里保存username
    req.session.flush()
    return HttpResponseRedirect('/')
