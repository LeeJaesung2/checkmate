from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Write
from survey.models import SurveyEssential, SurveyOptional
from checkmate.models import Scrap_roommate
from account.models import CustomUser
from datetime import datetime
import math


# Create your views here.

def searchRoommate(request):
    if request.user.is_authenticated:
        survey_ess, survey_opt = surveycheck(request)
        search_keyword = request.GET.get('search_keyword')
        writes = Write.objects.all().order_by('-id')
        writes = filter(request, writes)
        if search_keyword:
            if len(search_keyword) > 1:
                writes = writes.filter(title__icontains=search_keyword)
                writes, page_range, next_page, pre_page = paging(request, writes)
                return render(request, 'searchRoommate.html',{'writes':writes,'search_keyword':search_keyword, 'page_range':page_range, 'next_page':next_page, 'pre_page':pre_page})
            else:
                messages.error(request, '검색어는 2글자 이상 입력해주세요')
        writes, page_range, next_page, pre_page = paging(request, writes)
        
        if CustomUser.objects.get(id=request.user.id).survey_ess_id:
            mysurvey_ess_id = CustomUser.objects.get(id=request.user.id).survey_ess_id.id
            mysurvey = list(SurveyEssential.objects.filter(id = mysurvey_ess_id).values())[0]
            mysurvey_value = list(mysurvey.values())[2:]
            fitness_str = ''
            for writer in writes:
                persentage = 0
                index = 0
                matchcnt = 0
                othersurvey_ess_id = writer.user_id.survey_ess_id.id
                if othersurvey_ess_id == mysurvey_ess_id :
                    fitness_str += "100,"
                else :
                    othersurvey = list(SurveyEssential.objects.filter(id = othersurvey_ess_id).values())[0]
                    othersurvey_value = list(othersurvey.values())[2:]
                    for i in mysurvey_value:
                        if i == othersurvey_value[index]:
                            if 2<index<7:
                                matchcnt+=0.25
                            elif 7<index<10:
                                mytime = mysurvey_value[index].hour*60 + mysurvey_value[index].minute

                                othertime = othersurvey_value[index].hour*60 + othersurvey_value[index].minute

                                temp = mytime - othertime
                                if -60<temp<60:
                                    matchcnt+=1
                                elif -90<temp<90:
                                    matchcnt+=0.75
                                elif -120<temp<120:
                                    matchcnt+=0.5
                        # elif index == 12:
                        #     temp = i - othersurvey[index]
                        #     if -1<i<1:
                        #         matchcnt+=1
                        #     elif -2<i<2:
                        #         matchcnt+=0.75
                            else:
                                matchcnt += 1
                        index += 1
                    persentage = matchcnt/index*100
                fitness = "%0.1f" %persentage
                fitness_str += str(fitness)+","
            return render(request, 'searchRoommate.html',{'writes':writes, 'page_range':page_range, 'survey_ess':survey_ess, 'survey_opt':survey_opt, 'next_page':next_page, 'pre_page':pre_page,'fitness_str':fitness_str})
        return render(request, 'searchRoommate.html',{'writes':writes, 'page_range':page_range, 'next_page':next_page, 'pre_page':pre_page})
    
    else:
        a = 1 
        # 로그인 안된 상태 확인
        search_keyword = request.GET.get('search_keyword')
        writes = Write.objects.all().order_by('-id')
        writes = filter(request, writes)
        if search_keyword:
            if len(search_keyword) > 1:
                writes = writes.filter(title__icontains=search_keyword)
                writes, page_range, next_page, pre_page = paging(request, writes)
                return render(request, 'searchRoommate.html',{'writes':writes,'search_keyword':search_keyword, 'page_range':page_range, 'next_page':next_page, 'pre_page':pre_page})
            else:
                messages.error(request, '검색어는 2글자 이상 입력해주세요')
        writes, page_range, next_page, pre_page = paging(request, writes)
        return render(request, 'searchRoommate.html',{'writes':writes, 'page_range':page_range, 'next_page':next_page, 'pre_page':pre_page,'a':a})

def detail(request, write_id):
    write_detail = get_object_or_404(Write, pk=write_id)
    survey_ess = write_detail.user_id.survey_ess_id
    survey_opt = write_detail.user_id.survey_opt_id
    age = datetime.today().year - write_detail.user_id.user_birthyear+1
    pre = write_detail.id - 1
    next = write_detail.id + 1
    scrap = request.GET.get("Favorites")
    aleady = Scrap_roommate.objects.all()
    if(request.user.id):
        user_id = CustomUser.objects.get(id=request.user.id)
        aleady = aleady.filter(write=write_detail)
        aleady = aleady.filter(user_id=user_id)
    if(scrap):
        if aleady:
            messages.error(request, '이미 스크랩된 게시물 입니다')
            fail = 1
        else:
            scrap = Scrap_roommate()
            scrap.user_id = user_id
            scrap.write = write_detail
            scrap.save()
            fail = 0
        return render(request, 'detail.html',{'write_detail':write_detail,'survey_ess':survey_ess,'survey_opt':survey_opt, 'age':age, 'pre':pre, 'next':next, 'fail':fail})
    if aleady:
        okscrap = 0
    else:
        okscrap = 1
    return render(request, 'detail.html',{'write_detail':write_detail,'survey_ess':survey_ess,'survey_opt':survey_opt, 'age':age, 'pre':pre, 'next':next, 'okscrap':okscrap})

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
    



def year(age):
    now = datetime.today().year
    year = now - int(age) +1
    return (year)

def filter(request, writes):
    state = request.GET.get('state')
    if state:
        writes = writes.filter(state=state)

    age_start = request.GET.get('age_start')
    age_end = request.GET.get('age_end')
    
    if age_start and age_end:
        
        year_end = year(age_start)
        yser_start = year(age_end)
        writes = writes.filter(user_id__user_birthyear__range=(yser_start,year_end))

    grad = request.GET.get('grad')
    if grad:
        writes = writes.filter(survey_ess_id__grade=grad)

    room_type = request.GET.get('room_type')
    if room_type:
        writes = writes.filter(survey_ess_id__room_type=room_type)

    dormitory_number_man = request.GET.get('dormitory_number_man')
    dormitory_number_woman = request.GET.get('dormitory_number_woman')
    dormitory_number = request.GET.get('dormitory_number')
    if dormitory_number_man:
        writes = writes.filter(survey_ess_id__dormitory_number_man=dormitory_number_man)
    if dormitory_number_woman:
        writes = writes.filter(survey_ess_id__ormitory_number_woman=dormitory_number_woman)
    if dormitory_number=='10' or dormitory_number=='8' or dormitory_number=='6' or dormitory_number=='3' or dormitory_number=='2' or dormitory_number=='1':
        writes = writes.filter(survey_ess_id__dormitory_number_man=dormitory_number)
    if dormitory_number=='11' or dormitory_number=='9' or dormitory_number=='7' or dormitory_number=='5' or dormitory_number=='4':
        writes = writes.filter(survey_ess_id__dormitory_number_woman=dormitory_number)


    dormitory_year_start = request.GET.get('dormitory_year_start')
    dormitory_semester_start = request.GET.get('dormitory_semester_start')
    if dormitory_year_start and dormitory_semester_start:
        writes = writes.filter(survey_ess_id__dormitory_year_start=dormitory_year_start)
        writes = writes.filter(survey_ess_id__dormitory_semester_start=dormitory_semester_start)

    dormitory_year_end = request.GET.get('dormitory_year_end')
    dormitory_semester_end = request.GET.get('dormitory_semester_end')
    if dormitory_year_end and dormitory_semester_end:
        writes = writes.filter(survey_ess_id__dormitory_year_end=dormitory_year_end)
        writes = writes.filter(survey_ess_id__dormitory_semester_end=dormitory_semester_end)

    
    relationship = request.GET.get('relationship')
    if relationship:
        writes = writes.filter(survey_ess_id__relationship=relationship)

    start_wakeup_time = request.GET.get('start_wakeup_time')
    end_wakeup_time = request.GET.get('end_wakeup_time')
    if start_wakeup_time and end_wakeup_time:
        writes = writes.filter(survey_ess_id__wakeup_time__range=(start_wakeup_time,end_wakeup_time))

    start_bed_time = request.GET.get('start_bed_time')
    end_bed_time = request.GET.get('end_bed_time')
    if start_bed_time and end_bed_time:
        writes = writes.filter(survey_ess_id__bed_time__range=(start_bed_time,end_bed_time))

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

    animal_dog = request.GET.get('animal_dog')
    if animal_dog:
        writes = writes.filter(survey_ess_id__animal_dog=animal_dog)
    animal_cat = request.GET.get('animal_cat')
    if animal_cat:
        writes = writes.filter(survey_ess_id__animal_cat=animal_cat)
    animal_no = request.GET.get('animal_no')
    if animal_no:
        writes = writes.filter(survey_ess_id__animal_no=animal_no)



    share = request.GET.get('share')
    if share:
        writes = writes.filter(survey_opt_id__share=share)

    toilet = request.GET.get('toilet')
    if toilet:
        writes = writes.filter(survey_opt_id__toilet=toilet)
    
    ventilate = request.GET.get('ventilate')
    if ventilate:
        writes = writes.filter(survey_opt_id__ventilate=ventilate)

    feel_cold = request.GET.get('feel_cold')
    if feel_cold:
        writes = writes.filter(survey_opt_id__feel_cold=feel_cold)
    feel_hot = request.GET.get('feel_hot')
    if feel_hot:
        writes = writes.filter(survey_opt_id__feel_hot=feel_hot)

    bug = request.GET.get('bug')
    if bug:
        writes = writes.filter(survey_opt_id__bug=bug)

    keyboard = request.GET.get('keyboard')
    if keyboard:
        writes = writes.filter(survey_opt_id__keyboard=keyboard)
    keyboard_checkbox = request.GET.get('keyboard_checkbox')
    if keyboard_checkbox:
        writes = writes.filter(survey_opt_id__keyboard_noise=keyboard_checkbox)

    game = request.GET.get('game')
    if game:
        writes = writes.filter(survey_opt_id__game=game)

    mbti = request.GET.get('mbti')
    if mbti:
        writes = writes.filter(survey_opt_id__mbti=mbti)
    
    return(writes)

def paging(request, writes):
    page = int(request.GET.get('page',1))
    next_page = int(request.GET.get('page',1))+1
    pre_page = int(request.GET.get('page',1))-1
    paginated_by = 10
    total_count = len(writes)
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
    writes = writes[start_index:end_index]

    return writes, page_range, next_page, pre_page

def surveycheck(request):
    user_id = CustomUser.objects.get(id=request.user.id)
    survey_ess = user_id.survey_ess_id
    survey_opt = user_id.survey_opt_id
    return survey_ess, survey_opt
