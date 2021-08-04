from django.shortcuts import render, redirect
from checkmate.models import Offcampus_Post,Domitory_Post
from account.models import CustomUser
from django.utils import timezone

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
        post.pub_date = timezone.now()
        post.save()
        return redirect('offcampusView', post.id)
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
        post.pub_date = timezone.now()
        post.save()
        return redirect('domitoryCommunity', post.id)
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

def offcampusView(request,post_id):
    
    post = Offcampus_Post.objects.get(id=post_id)
    return render(request, 'offcampusView.html',{'post':post})

def domitoryView(request,post_id):

    post = Domitory_Post.objects.get(id=post_id)
    return render(request, 'domitoryView.html',{'post':post})

def offcampusDelete(request, post_id):
    post = Offcampus_Post.objects.get(id=post_id)
    post.delete()
    return redirect('offcampusCommunity')

def domitoryDelete(request, post_id):
    post = Domitory_Post.objects.get(id=post_id)
    post.delete()
    return redirect('domitoryCommunity')