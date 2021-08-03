from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Write
from survey.models import SurveyEssential, SurveyOptional
from account.models import CustomUser

# Create your views here.

def searchRoommate(request):
    search_keyword = request.GET.get('search_keyword')
    writes = Write.objects
    writes = filter(request, writes)
    if search_keyword:
        if len(search_keyword) > 1:
            writes = writes.filter(title__icontains=search_keyword)
            return render(request, 'searchRoommate.html',{'writes':writes,'search_keyword':search_keyword})
        else:
            messages.error(request, '검색어는 2글자 이상 입력해주세요')
    return render(request, 'searchRoommate.html',{'writes':writes})

def detail(request, write_id):
    write_detail = get_object_or_404(Write, pk=write_id)
    survey_ess = write_detail.user_id.survey_ess_id
    survey_opt = write_detail.user_id.survey_opt_id
    return render(request, 'detail.html',{'write_detail':write_detail,'survey_ess':survey_ess,'survey_opt':survey_opt})

def create(request):
    if request.method == 'POST':
        write = Write()
        write.title = request.POST.get('title')
        write.body = request.POST.get('body')
        write.state = request.POST.get('state')
        user_id = CustomUser.objects.get(id=request.POST.get('user_id'))
        write.user_id =  user_id
        write.survey_ess_id =  user_id.survey_ess_id
        write.survey_opt_id = user_id.survey_opt_id
        write.save()
        return redirect('/roommate/detail/'+str(write.id))
    else:
        user_id = request.user.id
    return render(request, 'create.html',{'user_id':user_id})

def update(request, write_id):
    write = Write.objects.get(id=write_id)
    if request.method == "POST":
        instanc=write
        write.title = request.POST.get('title')
        write.body = request.POST.get('body')
        write.state = request.POST.get('state')
        write.save()
        return redirect('/roommate/detail/'+str(write_id))
    else:
        return render(request, 'update.html', {'write':write})
        
def delete(request, write_id):
    write = Write.objects.get(id=write_id)
    write.delete()
    return redirect('searchRoommate')
    





def filter(request, writes):
    room_type = request.GET.get('room_type')
    if room_type:
        writes = writes.filter(survey_ess_id__room_type=room_type)
    
    relationship = request.GET.get('relationship')
    if relationship:
        writes = writes.filter(survey_ess_id__relationship=relationship)

    smoke = request.GET.get('smoke')
    if smoke:
        writes = writes.filter(survey_ess_id__smoke=smoke)

    cleaning = request.GET.get('cleaning')
    if cleaning:
        writes = writes.filter(survey_ess_id__cleaning=cleaning)

    sleeping_habits_snoring = request.GET.get('sleeping_habits_snoring')
    if sleeping_habits_snoring:
        writes = writes.filter(survey_ess_id__sleeping_habits_snoring=sleeping_habits_snoring)
    sleeping_habits_teeth = request.GET.get('sleeping_habits_teeth')
    if sleeping_habits_teeth:
        writes = writes.filter(survey_ess_id__sleeping_habits_teeth=sleeping_habits_teeth)
    sleeping_habits_nothing = request.GET.get('sleeping_habits_nothing')
    if sleeping_habits_nothing:
        writes = writes.filter(survey_ess_id__sleeping_habits_nothing=sleeping_habits_nothing)

    invite_friends = request.GET.get('invite_friends')
    if invite_friends:
        writes = writes.filter(survey_ess_id__invite_friends=invite_friends)

    call = request.GET.get('call')
    if call:
        writes = writes.filter(survey_ess_id__call=call)

    earphones = request.GET.get('earphones')
    if earphones:
        writes = writes.filter(survey_ess_id__earphones=earphones)

    eat = request.GET.get('eat')
    if eat:
        writes = writes.filter(survey_ess_id__eat=eat)


    toilet = request.GET.get('toilet')
    if toilet:
        writes = writes.filter(survey_opt_id__toilet=toilet)
    
    ventilate = request.GET.get('ventilate')
    if ventilate:
        writes = writes.filter(survey_opt_id__ventilate=ventilate)

    bug = request.GET.get('bug')
    if bug:
        writes = writes.filter(survey_opt_id__bug=bug)

    keyboard = request.GET.get('keyboard')
    if keyboard:
        writes = writes.filter(survey_opt_id__keyboard=keyboard)

    game = request.GET.get('game')
    if game:
        writes = writes.filter(survey_opt_id__game=game)

    mbti = request.GET.get('mbti')
    if mbti:
        writes = writes.filter(survey_opt_id__mbti=mbti)
    return(writes)