from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout,update_session_auth_hash
from .forms import RegisterForm
from django.contrib.auth.hashers import check_password

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request=request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
        return redirect('main')
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form':form})


def logout_view(request):
    logout(request)
    return redirect('main')

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
        return redirect('main')
    else:
        form = RegisterForm()
        return render(request, 'register.html', {'form':form})

def change_password(request):
    context = {}
    if request.method == 'POST':
        current_password = request.POST.get('user_password')
        user = request.user
        if check_password(current_password,user.password):
            new_password = request.POST.get('password1')
            new_password_check = request.POST.get('password2')
            if new_password == new_password_check :
                user.set_password(new_password)
                user.save()
                login(request,user)
                return redirect('main')
            else:
                context.update({'error' : "새로입력한 비밀번호가 일치하지 않습니다."})
        else:
            context.update({'error' : "현재 비밀번호가 일치하지 않습니다."})
    return render(request, 'change_password.html', context)