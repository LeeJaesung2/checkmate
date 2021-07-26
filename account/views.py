from django.shortcuts import render, redirect
from django.contrib import auth,messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate, login, logout,update_session_auth_hash
from .forms import RegisterForm

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
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, '비밀번호가 변경되었습니다.')
            return redirect('change_password')
        else:
            messages.error(request, '비밀번호를 확인해주세요')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'mypageProfile', {'form': form})