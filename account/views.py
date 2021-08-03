from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
import requests
import json
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
            auth.login(request,user)
        return redirect('main')
    else:
        _token = request.session['access_token']
        _url = 'https://kapi.kakao.com/v2/user/me'
        _header = {'Authorization': f'bearer {_token}'}
        _res = requests.post(_url, headers=_header)
        kakao_id_json = json.loads(((_res.text).encode('utf-8')))
        kakao_id = kakao_id_json["id"]
        form = RegisterForm()
        return render(request, 'register.html',{'form':form, 'kakao_id':kakao_id})


def mypageProfile(request):
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
    return render(request, 'mypageProfile.html', context)



def kakaoLoginLogic(request):
    _restApiKey = 'f9d119f1d082709b083b6ee7e2333682'
    _redirectUrl = 'http://127.0.0.1:8000/account/kakaoLoginLogicRedirect'
    _url = f'https://kauth.kakao.com/oauth/authorize?client_id={_restApiKey}&redirect_uri={_redirectUrl}&response_type=code'
    return redirect(_url)

def kakaoLoginLogicRedirect(request):
    _qs = request.GET['code']
    _restApiKey = 'f9d119f1d082709b083b6ee7e2333682'
    _redirect_uri = 'http://127.0.0.1:8000/account/kakaoLoginLogicRedirect'
    _url = f'https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={_restApiKey}&redirect_uri={_redirect_uri}&code={_qs}'
    _res = requests.post(_url)
    _result = _res.json()
    request.session['access_token'] = _result['access_token']
    request.session.modified = True
    return redirect('register')

# def kakaoLogout(request):
#     _token = request.session['access_token']
#     _url = 'https://kapi.kakao.com/v1/user/logout'
#     _header = {
#       'Authorization': f'bearer {_token}'
#     }
#     _res = requests.post(_url, headers=_header)
#     _result = _res.json()
#     if _result.get('id'):
#         del request.session['access_token']
#         return render(request, 'main.html')
#     else:
#         return render(request, 'login.html')