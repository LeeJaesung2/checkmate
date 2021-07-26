from django.db import models
from account.models import CustomUser
import datetime

# Create your models here.

class SurveyEssential(models.Model):
    #기본키
    survey_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    #학년
    grade_choice = (
        ('1', '1학년'), 
        ('2', '2학년'),
        ('3', '3학년'),
        ('4', '4학년'),
        ('5', '5학년'),
        ('6', '6학년'),
        )
    grade = models.CharField(max_length=1, choices=grade_choice, default='1')
    #기숙사or자취
    room_type_choice = (
        ('0', '기숙사'), 
        ('1', '자취'),
    )
    room_type = models.CharField(max_length=1, choices=room_type_choice, default='0')
    #기숙사동
    dormitory_number_man_choice = (
        ('10', '10동'), 
        ('8', '8동'),
        ('6', '6동'),
        ('3', '3동'),
        ('2', '2동'),
        ('1', '1동'),
        )
    dormitory_number_man = models.CharField(max_length=2, choices=dormitory_number_man_choice, default='10', null=True, blank=True)
    dormitory_number_woman_choice = (
        ('11', '11동'), 
        ('9', '9동'),
        ('7', '7동'),
        ('5', '5동'),
        ('4', '4동'),
        )
    dormitory_number_woman = models.CharField(max_length=2, choices=dormitory_number_woman_choice, default='11', null=True, blank=True)
    #룸메와 함께할 시간
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
    #룸메와의 관계
    relationship_choice = (
    ('0', '친하게'), 
    ('1', '인사만'),
    )
    relationship = models.CharField(max_length=1, choices=relationship_choice, default='0')
    #자고 일어나는 시간
    wakeup_time = models.TimeField(default=datetime.time(9, 0))
    bed_time = models.TimeField(default=datetime.time(23, 0))
    #흡연 여부
    smoke = models.NullBooleanField(default=False)
    #청소 주기
    cleaning = models.IntegerField(default="3")
    #잠버릇
    sleeping_habits_snoring = models.NullBooleanField(default=False)
    sleeping_habits_teeth = models.NullBooleanField(default=False)
    sleeping_habits_other = models.CharField(max_length=10)
    sleeping_habits_nothing = models.NullBooleanField(default=False)
    #친구초대여부
    invite_friends = models.NullBooleanField(default=False)
    #통화가능여부
    call_choice = (
        ('0', '예'), 
        ('1', '아니요'),
        ('2', '짧은 통화만')
    )
    call = models.CharField(max_length=1, choices=call_choice, default='0')
    #이어폰 사용여부
    earphones = models.NullBooleanField(default=True)
    #실내 취식
    eat_choice = (
        ('0', '식사도 방안에서'), 
        ('1', '냄새 안 나는 음식만(간식)'),
        ('2', '나가서 먹음'),
    )
    eat = models.CharField(max_length=1, choices=eat_choice, default='0')

    def __str__(self):
        return str(self.survey_id)


class SurveyOptional(models.Model):
    survey_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    share = models.NullBooleanField()
    toilet = models.IntegerField(null=True, blank=True)
    ventilate = models.IntegerField(null=True, blank=True)
    #더위·추위 탐
    feel_cold = models.NullBooleanField()
    feel_hot = models.NullBooleanField()
    #벌레
    bug = models.NullBooleanField()
    #키보드
    keyboard_choice = (
        ('0', '타이핑&게임 자주함'), 
        ('1', '거의 안함'),
    )
    keyboard = models.CharField(max_length=1, choices=keyboard_choice, null=True, blank=True)
    keyboard_noise = models.NullBooleanField()
    #게임
    game_choice = (
        ('0', '자주'), 
        ('1', '가끔'),
        ('2', '안함'),
    )
    game = models.CharField(max_length=1, choices=game_choice, null=True, blank=True)
    
    def __str__(self):
        return str(self.survey_id)