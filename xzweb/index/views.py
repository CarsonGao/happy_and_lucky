from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def page_login(request):
    return render(request, 'page_login.html')

def page_registration(request):
    return render(request, 'page_registration.html')