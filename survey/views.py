from django.shortcuts import render
from .models import SurveyEssential, SurveyOptional


# Create your views here.

def survey(request):
    return render(request, 'survey.html')

def submitSurvey(request):
    print("쿼리 출력: ", request.POST)

    eSurvey = SurveyEssential() #EssentialSurvey
    eSurvey.survey_id = request.user
    eSurvey.grade = request.POST['grade']
    eSurvey.room_type = request.POST['room-type']
    eSurvey.dormitory_number = request.POST['dormitory-number']
    eSurvey.dormitory_year_start = request.POST['dormitory-year-start']
    eSurvey.save()

    return render(request, 'survey.html')