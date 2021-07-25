from django.contrib import admin
from .models import SurveyEssential, SurveyOptional

# Register your models here.

admin.site.register(SurveyEssential)
admin.site.register(SurveyOptional)

