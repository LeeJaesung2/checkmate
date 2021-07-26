from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request,'main.html')

def infoWrite(request):
    return render(request, 'infoWrite.html')

def survey(request):
    return render(request, 'survey.html')