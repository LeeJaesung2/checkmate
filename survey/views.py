from django.shortcuts import render
from .models import SurveyEssential, SurveyOptional
from account.models import CustomUser

# Create your views here.

def survey(request):
    return render(request, 'survey.html')

def submitSurvey(request):
    user_id = request.user.id
    user_obj = CustomUser.objects.get(id=user_id)

    eSurvey = SurveyEssential() #EssentialSurvey
    eSurvey.grade = request.POST['grade']
    eSurvey.room_type = request.POST['room-type']
    if user_obj.user_gender == 'man':
        eSurvey.dormitory_number_man = request.POST['dormitory-number-man']
    else:
        eSurvey.dormitory_number_woman = request.POST.get('dormitory-number-woman')
    eSurvey.dormitory_year_start = request.POST['dormitory-year-start']
    eSurvey.dormitory_semester_start = request.POST['dormitory-semester-start']
    eSurvey.dormitory_year_end = request.POST['dormitory-year-end']
    eSurvey.dormitory_semester_end = request.POST['dormitory-semester-end']
    eSurvey.relationship = request.POST.get('relationship')
    eSurvey.wakeup_time = request.POST['wakeup-time']
    eSurvey.bed_time = request.POST['bed-time']
    eSurvey.smoke = request.POST.get('smoke')
    eSurvey.cleaning = request.POST['cleaning']
    eSurvey.sleeping_habits_snoring = True if request.POST.get('sleeping-habits-snoring')=='on' else False
    eSurvey.sleeping_habits_teeth = True if request.POST.get('sleeping-habits-teeth')=='on' else False
    eSurvey.sleeping_habits_nothing = True if request.POST.get('sleeping-habits-nothing')=='on' else False
    # eSurvey.sleeping_habits_snoring = request.POST.get('sleeping-habits-snoring')
    # eSurvey.sleeping_habits_teeth = request.POST['sleeping-habits-teeth']
    # eSurvey.sleeping_habits_nothing = request.POST.get('sleeping-habits-nothing')
    eSurvey.sleeping_habits_other = request.POST.get('sleeping-habits-other')
    eSurvey.invite_friends = request.POST.get('invite-friends')
    eSurvey.call = request.POST.get('call')
    eSurvey.earphones = request.POST.get('earphones')
    eSurvey.eat = request.POST.get('eat')
    eSurvey.animal_dog = True if request.POST.get('animial-dog')=='on' else False
    eSurvey.animal_cat = True if request.POST.get('animial-cat')=='on' else False
    eSurvey.animal_no = True if request.POST.get('animial-no')=='on' else False
    eSurvey.animal_other = request.POST.get('animal-other')
    eSurvey.save()

    oSurvey = SurveyOptional()
    oSurvey.share = request.POST['share']
    oSurvey.toilet = request.POST['toilet']
    oSurvey.ventilate = request.POST['ventilate']
    oSurvey.feel_cold = True if request.POST.get('feel-cold')=='on' else False
    oSurvey.feel_hot = True if request.POST.get('feel-hot')=='on' else False
    oSurvey.bug = request.POST.get('bug')
    oSurvey.keyboard = request.POST.get('keyboard')
    oSurvey.keyboard_noise = True if request.POST.get('keyboard-checkboxg')=='on' else False
    oSurvey.game = request.POST.get('game')
    oSurvey.mbti = request.POST['mbti']
    oSurvey.save()

    user_obj.survey_ess_id = eSurvey
    user_obj.survey_opt_id = oSurvey
    user_obj.save()

    return render(request, 'survey.html')