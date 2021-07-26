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
    eSurvey.dormitory_semester_start = request.POST['dormitory-semester-start']
    eSurvey.dormitory_year_end = request.POST['dormitory-year-end']
    eSurvey.dormitory_semester_end = request.POST['dormitory-semester-end']
    eSurvey.relationship = request.POST['relationship']
    eSurvey.wakeup_time = request.POST['wakeup-time']
    eSurvey.bed_time = request.POST['bed-time']
    eSurvey.smoke = request.POST['smoke']
    eSurvey.cleaning = request.POST['cleaning']
    eSurvey.sleeping_habits_snoring = True if request.POST.get('sleeping-habits-snoring')=='on' else False
    eSurvey.sleeping_habits_teeth = True if request.POST.get('sleeping-habits-teeth')=='on' else False
    eSurvey.sleeping_habits_nothing = True if request.POST.get('sleeping-habits-nothing')=='on' else False
    # eSurvey.sleeping_habits_snoring = request.POST.get('sleeping-habits-snoring')
    # eSurvey.sleeping_habits_teeth = request.POST['sleeping-habits-teeth']
    # eSurvey.sleeping_habits_nothing = request.POST.get('sleeping-habits-nothing')
    eSurvey.sleeping_habits_other = request.POST['sleeping-habits-other']
    eSurvey.invite_friends = request.POST['invite-friends']
    eSurvey.call = request.POST['call']
    eSurvey.earphones = request.POST['earphones']
    eSurvey.eat = request.POST['eat']
    eSurvey.save()

    return render(request, 'survey.html')