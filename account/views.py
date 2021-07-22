from django.shortcuts import render, redirect
from django.utils import timezone
from .models import CustomUser

# Create your views here.

def login_view(request):
    return render(request,'login.html')

def logout_view(request):
    return render(request,'login.html')

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