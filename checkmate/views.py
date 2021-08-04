from django.shortcuts import render, redirect
from checkmate.models import Offcampus_Post,Domitory_Post
from account.models import CustomUser

# Create your views here.

def main(request):
    return render(request,'main.html')

def infoWrite(request):
    if request.method == 'POST':
        post = Offcampus_Post()
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.preface = request.POST.get('preface')
        post.preface_2 = request.POST.get('preface_2')
        user_id = request.POST.get('user_id')
        user = CustomUser.objects.get(id=user_id)
        post.user_id = user
        post.save()
        return redirect('offcampusCommunity')
    else:
        user = request.user
        return render(request, 'infoWrite.html',{'user':user})


def dom_infoWrite(request):
    if request.method == 'POST':
        post = Domitory_Post()
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.preface = request.POST.get('preface')
        post.preface_2 = request.POST.get('preface_2')
        user_id = request.POST.get('user_id')
        user = CustomUser.objects.get(id=user_id)
        post.user_id = user
        post.save()
        return redirect('domitoryCommunity')
    else:
        user = request.user
        return render(request, 'dom_infoWrite.html',{'user':user})

def survey(request):
    return render(request, 'survey.html')

def mypageScrap(request):
    return render(request, 'mypageScrap.html')

def mypageWritten(request):
    return render(request, 'mypageWritten.html')

def offcampusCommunity(request):
    posts = Offcampus_Post.objects.all()

    return render(request, 'offcampusCommunity.html',{'posts':posts})


def domitoryCommunity(request):
    posts = Domitory_Post.objects.all()

    return render(request, 'domitoryCommunity.html',{'posts':posts})
