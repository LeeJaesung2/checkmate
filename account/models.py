from django.db import models

# Create your models here.
class CustomUser(models.Model):
    user_id = models.CharField(max_length=32, unique=True, verbose_name='아이디')
    user_password = models.CharField(max_length=128, verbose_name='비밀번호')
    user_name = models.CharField(max_length=16, unique=True, verbose_name='이름')
    user_gender = models.CharField(max_length=8, unique=True, verbose_name='성별')
    user_nation = models.CharField(max_length=16, unique=True, verbose_name='국적')
    user_nickname = models.CharField(max_length=32, unique=True, verbose_name='닉네임')
    user_register_time = models.DateTimeField(auto_now_add=True,verbose_name='계정생성 시간')

def __str__(self):
    return slef.user_name

class Meta:
    db_table = 'user'
    verbose_name = '유저'
    verbose_name_plural = '유저'