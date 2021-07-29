from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q
from .models import Write

# Create your views here.

def searchRoommate(request):
    writes = Write.objects
    return render(request, 'searchRoommate.html',{'writes':writes})

def detail(request, ):
    return render(request, 'detail.html')





# def create_detail(request):
#     if request.method == "POST":

        

# def get_queryset(self):
#     search_keyword = self.request.GET.get('q','')
#     survey_list = Survey.objects()

#     if search_keyword :
#         if len(search_keyword) > 1:
#             search_survey_list = survey_list.filter(title__icontains=search_keyword)
#             return search_survey_list
#         else:
#             message.error(self.request, "검색어를 2글자 이상 입력해주세요.")
#     return survey_list

# def get_context_data(self, **kwargs):
#     search_keyword = self.request.GET.get('q', '')

#     if len(search_keyword) > 1 :
#         context['q'] = search_keyword

#     return context