from django.shortcuts import render
from .models import SurveyEssential, SurveyOptional


# Create your views here.

def survey(request):
    return render(request, 'survey.html')
