from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request,'main.html')


def infoWrite(request):
    return render(request, 'infoWrite.html')

def survey(request):
    return render(request, 'survey.html')

def mypageProfile(request):
    return render(request, 'mypageProfile.html')

def mypageScrap(request):
    return render(request, 'mypageScrap.html')

def mypageWritten(request):
    return render(request, 'mypageWritten.html')

def searchRoommate(request):
    return render(request, 'searchRoommate.html')

def detail(request):
    return render(request, 'detail.html')

def community(request):
    return render(request, 'community.html')