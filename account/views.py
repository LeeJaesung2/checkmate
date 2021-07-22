from django.shortcuts import render, redirect
from django.utils import timezone
from .models import CustomUser
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
    if request.method == 'POST':
        user_id = request.POST.get('id', '')
        user_password = request.POST.get('pw', '')
        user_password_check = request.POST.get('pw-check', '')
        user_name = request.POST.get('name', '')
        user_gender = request.POST.get('gender', '')
        user_nation = request.POST.get('nation', '')
        user_nickname = request.POST.get('nickname', '')

        if(user_id or user_password or user_password_check or user_name or user_gender or user_nation or user_nickname) == '':
            return redirect('/account/register',{'error' : '모든 항목을 입력해 주세요' })
        elif user_password != user_password_check:
            return redirect('/account/register',{'error' : 'password가 일치하지 않습니다' })
        else:
            customUser = CustomUser(
                user_id = user_id,
                user_password = user_password,
                user_password_check = user_password_check,
                user_name =  user_name,
                user_gender = user_gender,
                user_nation = user_nation,
                user_nickname = user_nickname,
                user_register_time = timezone.datetime.now()
            )
            customUser.save()
            # login(request,user)
        return redirect('main')
    else:
        return render(request,'register.html')