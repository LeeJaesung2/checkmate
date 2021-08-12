from django.shortcuts import render, redirect
from .models import SurveyEssential, SurveyOptional
from account.models import CustomUser
from datetime import datetime

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

        return redirect('searchRoommate')

def mypageCheckupdate(request):
    user_id = request.user.id
    user = CustomUser.objects.get(id=user_id)
    eSurvey = user.survey_ess_id
    oSurvey = user.survey_opt_id
    age = datetime.today().year - user.user_birthyear + 1

    if request.method == 'POST':
        age2 = request.POST['age']
        user.user_birthyear = datetime.today().year - int(age2)  + 1 
        user.save()
        eSurvey.grade = request.POST['grade']
        eSurvey.room_type = request.POST['room_type']
        if user.user_gender == 'man':
            eSurvey.dormitory_number_man = request.POST['dormitory-number-man']
        else:
            eSurvey.dormitory_number_woman = request.POST.get('dormitory_number_woman')
            eSurvey.dormitory_year_start = request.POST['dormitory_year_start']
            eSurvey.dormitory_semester_start = request.POST['dormitory_semester_start']
            eSurvey.dormitory_year_end = request.POST['dormitory_year_end']
            eSurvey.dormitory_semester_end = request.POST['dormitory_semester_end']
            eSurvey.relationship = request.POST.get('relationship')
            eSurvey.wakeup_time = request.POST['wakeup_time']
            eSurvey.bed_time = request.POST['bed_time']
            eSurvey.smoke = request.POST.get('smoke')
            eSurvey.cleaning = request.POST['cleaning']
            eSurvey.sleeping_habits_snoring = True if request.POST.get('sleeping_habits_snoring')=='on' else False
            eSurvey.sleeping_habits_teeth = True if request.POST.get('sleeping_habits_teeth')=='on' else False
            eSurvey.sleeping_habits_nothing = True if request.POST.get('sleeping_habits_nothing')=='on' else False
            eSurvey.sleeping_habits_other = request.POST.get('sleeping_habits_other')
            eSurvey.invite_friends = request.POST.get('invite_friends')
            eSurvey.call = request.POST.get('call')
            eSurvey.earphones = request.POST.get('earphones')
            eSurvey.eat = request.POST.get('eat')
            eSurvey.animal_dog = True if request.POST.get('animial_dog')=='on' else False
            eSurvey.animal_cat = True if request.POST.get('animial_cat')=='on' else False
            eSurvey.animal_no = True if request.POST.get('animial_no')=='on' else False
            eSurvey.animal_other = request.POST.get('animal_other')
            eSurvey.save()

            print(request.POST['wakeup_time'])
            print(request.POST['bed_time'])


            if request.POST.get('share'):
                oSurvey.share = request.POST.get('share')
            if request.POST.get('toilet'):
                oSurvey.toilet = request.POST.get('toilet')
            if request.POST.get('ventilate'): 
                oSurvey.ventilate = request.POST.get('ventilate')
            oSurvey.feel_cold = True if request.POST.get('feel_cold')=='on' else False
            oSurvey.feel_hot = True if request.POST.get('feel_hot')=='on' else False
            if request.POST.get('bug'): 
                oSurvey.bug = request.POST.get('bug')
            if request.POST.get('keyboard'): 
                oSurvey.keyboard = request.POST.get('keyboard')
            oSurvey.keyboard_noise = True if request.POST.get('keyboard_checkboxg')=='on' else False
            if request.POST.get('game'): 
                oSurvey.game = request.POST.get('game')
            if request.POST['mbti']: 
                oSurvey.mbti = request.POST['mbti']
            oSurvey.save()

        return redirect('mypageCheckupdate')
    else:
  

        return render(request, 'mypageCheckupdate.html',{'eSurvey':eSurvey, 'oSurvey':oSurvey,'user':user,'age':age})
        