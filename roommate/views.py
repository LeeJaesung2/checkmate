from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Write
from survey.models import SurveyEssential, SurveyOptional
from .forms import CreatePostForm

# Create your views here.

def searchRoommate(request):
    writes = Write.objects
    return render(request, 'searchRoommate.html',{'writes':writes})

def detail(request, write_id):
    write_detail = get_object_or_404(Write, pk=write_id)
    
    return render(request, 'detail.html',{'write_detail':write_detail})

def create(request):
    if request.method == 'POST':
        form = CreatePostForm(request.POST)
        if form.is_valid():
            write = form.save()
        return redirect('/roommate/detail/'+str(write.id))
    else:
        form = CreatePostForm()
    return render(request, 'create.html',{'form':form})

def update(request, wirte_id):
    write = Write.objects.get(id=write_id)
    if request.method == "POST":
        form = CreatePostForm(request.POST, instance=write)
        if form.is_valid():
            write = form.save()
            return redirect('/roommate/detail/'+str(write_id))
    else:
        form = CreatePostForm(instance=write)
        return render(request, 'create.html',{'form':form})
        
def delete(request, write_id):
    write = write.objects.get(id=write_id)
    write.delete()
    return redirect('searchRoommate')
    




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