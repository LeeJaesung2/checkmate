from django.shortcuts import render, redirect

# Create your views here.

def main(request):
    return render(request,'main.html')

def infoWrite(request):
    return render(request, 'infoWrite.html')

def survey(request):
    return render(request, 'survey.html')

def mypageScrap(request):
    return render(request, 'mypageScrap.html')

def mypageWritten(request):
    return render(request, 'mypageWritten.html')

def community(request):
    return render(request, 'community.html')

