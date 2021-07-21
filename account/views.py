from django.shortcuts import render

# Create your views here.

def login_views(request):
    return render(request,'login.html')

def logout_views(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')