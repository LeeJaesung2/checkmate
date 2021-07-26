from django.urls import path
from survey import views

urlpatterns = [
    path('', views.survey, name="survey"),
    path('submitSurvey', views.submitSurvey, name="submitSurvey"),

]