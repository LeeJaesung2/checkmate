from django.shortcuts import render, redirect
from checkmate.models import Offcampus_Post,Domitory_Post
from account.models import CustomUser
from .models import Scrap_roommate
from django.utils import timezone
from django.contrib import messages
from django.db.models import Q
import math
from datetime import datetime
from roommate.models import Write

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
        post.image = request.POST.get('image')
        user_id = request.POST.get('user_id')
        user = CustomUser.objects.get(id=user_id)
        post.user_id = user
        post.pub_date = timezone.now()
        post.save()
        return redirect('offcampusView', post.id)
    else:
        user = request.user
        if(user):
            return render(request, 'infoWrite.html',{'user':user})
        else:
            return redirect('offcampusCommunity')


def dom_infoWrite(request):
    if request.method == 'POST':
        post = Domitory_Post()
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.preface = request.POST.get('preface')
        post.preface_2 = request.POST.get('preface_2')
        post.image = request.POST.get('image')
        user_id = request.POST.get('user_id')
        user = CustomUser.objects.get(id=user_id)
        post.user_id = user
        post.pub_date = timezone.now()
        post.save()
        return redirect('domitoryView', post.id)
    else:
        user = request.user
        if(user):
            return render(request, 'dom_infoWrite.html',{'user':user})
        else:
            return redirect('domitoryCommunity')

def survey(request):
    return render(request, 'survey.html')

def mypageScrap(request):
    scraps = Scrap_roommate.objects.all()
    user_id = request.user.id
    scraps = scraps.filter(user_id__id=user_id)
    scraps, page_range = paging(request, scraps)
    return render(request, 'mypageScrap.html',{'scraps':scraps, 'page_range':page_range})


def mypageWritten(request):
    user=request.user
    o_posts = Offcampus_Post.objects.filter(user_id=user)
    d_posts = Domitory_Post.objects.filter(user_id=user)
    if request.method == 'POST':
        delete_array = request.POST.getlist('delete_array[]')

        num = 0
        for i in d_posts:
            if str(num) in delete_array:
                i.delete()
            num+=1

        for j in o_posts:
            if str(num) in delete_array:
                j.delete()
            num+=1
            print(delete_array)

        return redirect('mypageWritten')

    else:
        return render(request, 'mypageWritten.html',{'o_posts':o_posts,'d_posts':d_posts})


def offcampusCommunity(request):
    search_keyword = request.GET.get('search_keyword')
    posts = Offcampus_Post.objects.all().order_by('-pub_date','view')
    user_id = request.user.id
    if search_keyword:
        if len(search_keyword) > 1:
            posts = posts.filter(title__icontains=search_keyword)
            posts, page_range = paging(request, posts)
            return render(request, 'offcampusCommunity.html',{'posts':posts, 'search_keyword':search_keyword})
        else:
            message.error(request, '검색어는 2글자 이상 입력해주세요')
    posts, page_range = paging(request, posts)
    return render(request, 'offcampusCommunity.html',{'posts':posts, 'page_range':page_range,'user_id':user_id})

def domitoryCommunity(request):
    search_keyword = request.GET.get('search_keyword')
    posts = Domitory_Post.objects.all().order_by('-pub_date','view')
    user_id = request.user.id
    if search_keyword:
        if len(search_keyword) > 1:
            posts = posts.filter(title__icontains=search_keyword)
            posts, page_range = paging(request, posts)
            return render(request, 'domitoryCommunity.html',{'posts':posts, 'search_keyword':search_keyword, 'page_range':page_range})
        else:
            message.error(request, '검색어는 2글자 이상 입력해주세요')
    posts, page_range = paging(request, posts)
    return render(request, 'domitoryCommunity.html',{'posts':posts, 'page_range':page_range,'user_id':user_id})
     

def offcampusView(request,post_id):
    user = request.user
    post = Offcampus_Post.objects.get(id=post_id)
    post.view += 1 
    post.save()
    return render(request, 'offcampusView.html',{'post':post,'user':user})

def domitoryView(request,post_id):
    user = request.user
    post = Domitory_Post.objects.get(id=post_id)
    post.view += 1 
    post.save()
    return render(request, 'domitoryView.html',{'post':post,'user':user})

def offcampusDelete(request, post_id):
    post = Offcampus_Post.objects.get(id=post_id)
    post.delete()
    return redirect('offcampusCommunity')

def domitoryDelete(request, post_id):
    post = Domitory_Post.objects.get(id=post_id)
    post.delete()
    return redirect('domitoryCommunity')

def offcampusUpdate(request, post_id):
    if request.method == 'POST':
        post = Offcampus_Post.objects.get(id=post_id)
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.preface = request.POST.get('preface')
        post.preface_2 = request.POST.get('preface_2')
        post.image = request.POST.get('image')
        user_id = request.POST.get('user_id')
        user = CustomUser.objects.get(id=user_id)
        post.user_id = user
        post.pub_date = timezone.now()
        post.save()
        return redirect('offcampusView', post.id)
    else:
        post = Offcampus_Post.objects.get(id=post_id)
        user = request.user
        return render(request, 'offcampusUpdate.html',{'user':user,'post':post})


def domitoryUpdate(request, post_id):
    if request.method == 'POST':
        post = Domitory_Post.objects.get(id=post_id)
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.preface = request.POST.get('preface')
        post.preface_2 = request.POST.get('preface_2')
        post.image = request.POST.get('image')
        user_id = request.POST.get('user_id')
        user = CustomUser.objects.get(id=user_id)
        post.user_id = user
        post.pub_date = timezone.now()
        post.save()
        return redirect('offcampusView', post.id)
    else:
        post = Domitory_Post.objects.get(id=post_id)
        user = request.user
        return render(request, 'domitoryUpdate.html',{'user':user,'post':post})

def paging(request, posts):
    page = int(request.GET.get('page',1))
    paginated_by = 10
    total_count = len(posts)
    total_page = math.ceil(total_count/paginated_by)
    
    if (page<4):
        if (total_page<6):
            page_range = range(1, total_page+1)
        else:
            page_range = range(1, 6)

    else:
        if (total_page<page+3):
            page_range = range(total_page-4, total_page+1)
        else:
            page_range = range(page-2, page+3)

    start_index = paginated_by * (page-1)
    end_index = paginated_by * page
    posts = posts[start_index:end_index]

    return posts, page_range

def domitory_popular(request):
    posts=Domitory_Post.objects.filter(view__gte = 20).order_by('-pub_date')

    return render(request,'domitoryCommunity.html',{'posts':posts})

def offcampus_popular(request):
    posts=Offcampus_Post.objects.filter(view__gte = 20).order_by('-pub_date')

    return render(request,'offcampusCommunity.html',{'posts':posts})