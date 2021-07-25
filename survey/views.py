from django.shortcuts import render
from .models import SurveyEssential, SurveyOptional


# Create your views here.

def survey(request):
    return render(request, 'survey.html')

def createEssentialSurvey(request):
    eSurvey = SurveyEssential() #EssentialSurvey
    eSurvey.grade = request.GET['grade']
    eSurvey.room_type = request.GET['room-type']
    eSurvey.dormitory_number = request.GET['dormitory-number']
    eSurvey.dormitory_year_start = request.GET['dormitory-year-start']
    print(request.GET['room-type'])

    return render(request, 'survey.html')