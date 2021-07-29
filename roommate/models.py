from django.db import models
from survey.models import SurveyEssential, SurveyOptional

# Create your models here.

class Write(models.Model):
    grade = SurveyEssential.grade
    room_type = SurveyEssential.room_type
    if (SurveyEssential.dormitory_number_man is not None):
       dormitory_number = SurveyEssential.dormitory_number_man
    else:
        dormitory_number = dormitory_number_woman
    dormitory_year_start = SurveyEssential.dormitory_year_start
    dormitory_semester_start = SurveyEssential.dormitory_semester_start
    dormitory_year_end = SurveyEssential.dormitory_year_end
    dormitory_semester_end = SurveyEssential.dormitory_semester_end
    relationship = SurveyEssential.relationship
    wakeup_time = SurveyEssential.wakeup_time
    bed_time = SurveyEssential.bed_time
    smoke = SurveyEssential.smoke
    cleaning = SurveyEssential.cleaning
    sleeping_habits_snoring = SurveyEssential.sleeping_habits_snoring
    sleeping_habits_teeth = SurveyEssential.sleeping_habits_teeth
    sleeping_habits_other = SurveyEssential.sleeping_habits_other
    sleeping_habits_nothing = SurveyEssential.sleeping_habits_nothing
    invite_friends = SurveyEssential.invite_friends
    call = SurveyEssential.call
    earphones = SurveyEssential.earphones
    eat = SurveyEssential.eat
    animal = SurveyEssential.animal
    animal_other = SurveyEssential.animal_other
    share = SurveyOptional.share
    toilet = SurveyOptional.toilet
    ventilate = SurveyOptional.ventilate
    feel_cold = SurveyOptional.feel_cold
    feel_hot = SurveyOptional.feel_hot
    bug = SurveyOptional.bug
    keyboard = SurveyOptional.keyboard
    keyboard_noise = SurveyOptional.keyboard_noise
    game = SurveyOptional.game
    mbti = SurveyOptional.mbti

    title = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self):
        return self.title