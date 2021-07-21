from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def login_views(request):
    if request.method == 'POST':
        id = request.POST['user-id']
        password = request.POST['user-password']
        user = authenticate(request = request, username = id, password = password)
        if user is not None :
            login(request, user)
        return redirect('main')
    else :
        return render(request, 'login.html', {'error' : '일치하는 ID가 없어나 잘못된 Password 입니다.' })
    



def logout_views(request):
    logout(request)
    return redirect('main')

def register(request):
    return render(request,'register.html')