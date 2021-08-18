from django.shortcuts import render, redirect, get_object_or_404
from checkmate.models import Offcampus_Post,Domitory_Post
from account.models import CustomUser
from .models import Scrap_roommate, Scrap_dom, Scrap_off, Comment_dom, Comment_off
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
        if request.FILES.get('image') is not None:
            post.image = request.FILES.get('image')
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
        if request.FILES.get('image') is not None:
            post.image = request.FILES.get('image')
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
    #체크된 항목 삭제
    checked = request.POST.getlist('check[]')
    for check in checked:
        scrap = get_object_or_404(Scrap_roommate, pk=check)
        scrap.delete()
    user_id = request.user.id
    room_scraps = Scrap_roommate.objects.all().order_by('-id')
    room_scraps = room_scraps.filter(user_id__id=user_id)
    room_scraps, room_page_range, room_next_page, room_pre_page = paging(request, room_scraps)
    

    return render(request, 'mypageScrap.html',{'room_scraps':room_scraps,'room_page_range':room_page_range, 'room_next_page':room_next_page, 'room_pre_page':room_pre_page})

def mypageScrap_dom(request):
    checked = request.POST.getlist('check[]')
    for check in checked:
        scrap = get_object_or_404(Scrap_dom, pk=check)
        scrap.delete()
    user_id = request.user.id
    dom_scraps = Scrap_dom.objects.all().order_by('-id')
    dom_scraps = dom_scraps.filter(user_id__id=user_id)
    dom_scraps, dom_page_range, dom_next_page, dom_pre_page = paging(request, dom_scraps)
    return render(request, 'mypageScrap_dom.html',{'dom_scraps':dom_scraps, 'dom_page_range':dom_page_range, 'dom_next_page':dom_next_page, 'dom_pre_page':dom_pre_page})

def mypageScrap_off(request):
    checked = request.POST.getlist('check[]')
    for check in checked:
        scrap = get_object_or_404(Scrap_off, pk=check)
        scrap.delete()
    user_id = request.user.id
    off_scraps = Scrap_off.objects.all().order_by('-id')
    off_scraps = off_scraps.filter(user_id__id=user_id)
    off_scraps, off_page_range, off_next_page, off_pre_page = paging(request, off_scraps)
    return render(request, 'mypageScrap_off.html',{'off_scraps':off_scraps, 'off_page_range':off_page_range, 'off_next_page':off_next_page, 'off_pre_page':off_pre_page})


def mypageWritten(request):
    user=request.user
    d_posts = Domitory_Post.objects.filter(user_id=user)
    d_posts, dom_page_range, dom_next_page, dom_pre_page = paging(request, d_posts)
    return render(request, 'mypageWritten.html',{'d_posts':d_posts, 'dom_page_range':dom_page_range, 'dom_next_page':dom_next_page, 'dom_pre_page':dom_pre_page})

def mypageWritten_off(request):
    user=request.user
    o_posts = Offcampus_Post.objects.filter(user_id=user)
    o_posts, off_page_range, off_next_page, off_pre_page = paging(request, o_posts)
    return render(request, 'mypageWritten_off.html',{'o_posts':o_posts, 'off_page_range':off_page_range, 'off_next_page':off_next_page, 'off_pre_page':off_pre_page})


def offcampusCommunity(request):
    search_keyword = request.GET.get('search_keyword')
    posts = Offcampus_Post.objects.all().order_by('-pub_date','view')
    user_id = request.user.id
    if search_keyword:
        if len(search_keyword) > 1:
            posts = posts.filter(title__icontains=search_keyword)
            posts, page_range, next_page, pre_page = paging(request, posts)
            return render(request, 'offcampusCommunity.html',{'posts':posts, 'search_keyword':search_keyword, 'next_page':next_page, 'pre_page':pre_page})
        else:
            messages.error(request, '검색어는 2글자 이상 입력해주세요')
    posts, page_range, next_page, pre_page = paging(request, posts)
    return render(request, 'offcampusCommunity.html',{'posts':posts, 'page_range':page_range,'user_id':user_id, 'next_page':next_page, 'pre_page':pre_page})

def domitoryCommunity(request):
    search_keyword = request.GET.get('search_keyword')
    posts = Domitory_Post.objects.all().order_by('-pub_date','view')
    user_id = request.user.id
    if search_keyword:
        if len(search_keyword) > 1:
            posts = posts.filter(title__icontains=search_keyword)
            posts, page_range, next_page, pre_page = paging(request, posts)
            return render(request, 'domitoryCommunity.html',{'posts':posts, 'search_keyword':search_keyword, 'page_range':page_range, 'next_page':next_page, 'pre_page':pre_page})
        else:
            messages.error(request, '검색어는 2글자 이상 입력해주세요')
    posts, page_range, next_page, pre_page = paging(request, posts)
    return render(request, 'domitoryCommunity.html',{'posts':posts, 'page_range':page_range,'user_id':user_id, 'next_page':next_page, 'pre_page':pre_page})
     

def offcampusView(request,post_id):
    user = request.user
    post = Offcampus_Post.objects.get(id=post_id)
    post.view += 1 
    post.save()
    scrap = request.GET.get("Favorites")
    pre = post.id - 1
    next = post.id +1
    aleady = Scrap_off.objects.all()
    comments = Comment_off.objects.filter(write=post)
    if(request.user.id):
        user_id = CustomUser.objects.get(id=request.user.id)
        aleady = aleady.filter(Offcampus_Post=post)
        aleady = aleady.filter(user_id=user_id)
    if(scrap):
        if aleady:
            messages.error(request, '이미 스크랩된 게시물 입니다')
            fail = 1
        else:
            scrap = Scrap_off()
            scrap.user_id = user_id
            scrap.Offcampus_Post = post
            scrap.save()
            fail = 0
        return render(request, 'offcampusView.html',{'post':post,'user':user, 'pre':pre, 'next':next, 'fail':fail,'comments':comments})
    if aleady:
        okscrap = 0
    else:
        okscrap = 1
    return render(request, 'offcampusView.html',{'post':post,'user':user, 'pre':pre, 'next':next, 'okscrap':okscrap,'comments':comments})

def domitoryView(request,post_id):
    user = request.user
    post = Domitory_Post.objects.get(id=post_id)
    post.view += 1 
    post.save()
    scrap = request.GET.get("Favorites")
    pre = post.id - 1
    next = post.id +1
    aleady = Scrap_dom.objects.all()
    comments = Comment_dom.objects.filter(write=post)
    if(request.user.id):
        user_id = CustomUser.objects.get(id=request.user.id)
        aleady = aleady.filter(Domitory_Post=post)
        aleady = aleady.filter(user_id=user_id)
    if(scrap):
        if aleady:
            messages.error(request, '이미 스크랩된 게시물 입니다')
            fail = 1
        else:
            scrap = Scrap_dom()
            scrap.user_id = user_id
            scrap.Domitory_Post = post
            scrap.save()
            fail = 0
        return render(request, 'domitoryView.html',{'post':post,'user':user, 'pre':pre, 'next':next, 'fail': fail,'comments':comments})
    if aleady:
        okscrap = 0
    else:
        okscrap = 1
    return render(request, 'domitoryView.html',{'post':post,'user':user, 'pre':pre, 'next':next, 'okscrap':okscrap,'comments':comments})

def commnet_action_dom(request, post_id):
    write = get_object_or_404(Domitory_Post, pk=post_id)
    if(request.method == "POST"):
        comment = Comment_dom()
        comment.writer = CustomUser.objects.get(id=request.user.id).user_nickname
        comment.comment = request.POST.get("comment")
        comment.create_date = timezone.now()
        comment.write = write
        comment.save()
    return redirect('/domitoryView/'+str(post_id))

def commnet_action_off(request, post_id):
    write = get_object_or_404(Offcampus_Post, pk=post_id)
    if(request.method == "POST"):
        comment = Comment_off()
        comment.writer = CustomUser.objects.get(id=request.user.id).user_nickname
        comment.comment = request.POST.get("comment")
        comment.create_date = timezone.now()
        comment.write = write
        comment.save()
    return redirect('/offcampusView/'+str(post_id))

def comment_del_dom(request,post_id,comment_id):
    comment = get_object_or_404(Comment_dom,pk=comment_id)
    comment.delete()
    return redirect('/domitoryView/'+str(post_id))

def comment_del_off(request,post_id,comment_id):
    comment = get_object_or_404(Comment_off,pk=comment_id)
    comment.delete()
    return redirect('/offcampusView/'+str(post_id))

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
        return redirect('domitoryView', post.id)
    else:
        post = Domitory_Post.objects.get(id=post_id)
        user = request.user
        return render(request, 'domitoryUpdate.html',{'user':user,'post':post})

def paging(request, posts):
    page = int(request.GET.get('page',1))
    next_page = int(request.GET.get('page',1))+1
    pre_page = int(request.GET.get('page',1))-1
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

    return posts, page_range, next_page, pre_page

def domitory_popular(request):
    posts=Domitory_Post.objects.filter(view__gte = 20).order_by('-pub_date')

    return render(request,'domitoryCommunity.html',{'posts':posts})

def offcampus_popular(request):
    posts=Offcampus_Post.objects.filter(view__gte = 20).order_by('-pub_date')

    return render(request,'offcampusCommunity.html',{'posts':posts})
