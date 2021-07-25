from django.db import models
from account.models import CustomUser

# Create your models here.

class SurveyEssential(models.Model):
    #---기본키---#
    survey_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    #---학년---#
    grade = models.IntegerField()
    #---기숙사or자취---#
    room_type_choice = (
        ('0', '기숙사'), 
        ('1', '자취'),
    )
    room_type = models.CharField(max_length=1, choices=room_type_choice, default='0')
    #---기숙사동---#
    dormitory_number_choice = (
        ('10', '10동'), 
        ('8', '8동'),
        ('6', '6동'),
        ('3', '3동'),
        ('2', '2동'),
        ('1', '1동'),
        )
    dormitory_number = models.CharField(max_length=2, choices=dormitory_number_choice, default='10')
    #---룸메와 함께할 시간---#
    dormitory_year_choice = (
        ('2021', '2021년도'), 
        ('2022', '2022년도'),
        ('2023', '2023년도'),
    )
    dormitory_semester_choice = (
        ('1', '1학기'), 
        ('S', '여름방학'),
        ('2', '2학기'),
        ('W', '겨울방학'),
        )
    dormitory_year_start = models.CharField(max_length=4, choices=dormitory_year_choice, default='2021')
    dormitory_semester_start = models.CharField(max_length=1, choices=dormitory_semester_choice, default='1')
    dormitory_year_end = models.CharField(max_length=4, choices=dormitory_year_choice, default='2021')
    dormitory_semester_end = models.CharField(max_length=1, choices=dormitory_semester_choice, default='1')
    #---룸메와의 관계---#
    relationship_choice = (
    ('0', '친하게'), 
    ('1', '인사만'),
    )
    relationship = models.CharField(max_length=1, choices=relationship_choice, default='0')
    #---자고 일어나는 시간---#
    wakeup_time = models.DateField()
    bed_time = models.DateField()
    #---흡연 여부---#
    smoke = models.BooleanField()
    #---청소 주기---#
    cleaning = models.IntegerField()
    #---잠버릇---#
    sleeping_habit_choice = (
        ('0', '코골이'), 
        ('1', '이갈이'),
    )
    sleeping_habits = models.CharField(max_length=1, choices=sleeping_habit_choice, default='0')
    sleeping_habits_other = models.CharField(max_length=10)
    #---친구초대여부---#
    invite_friends = models.BooleanField()
    #---이어폰 사용여부---#
    earphone = models.BooleanField()
    #---실내 취식---#
    eat_choice = (
        ('0', '식사도 방안에서'), 
        ('1', '냄새 안 나는 음식만(간식)'),
        ('2', '나가서 먹음'),
    )
    eat = models.CharField(max_length=1, choices=eat_choice, default='0')

class SurveyOptional(models.Model):
    survey_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    share = models.BooleanField()
    toilet = models.IntegerField()
    ventilate = models.IntegerField()
    feel = models.IntegerField()
    bug = models.BooleanField()
    keyboard = models.IntegerField()
    game = models.BooleanField()