from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    user_name = models.CharField(max_length=16, verbose_name='이름')
    user_gender = models.CharField(max_length=8, verbose_name='성별')
    user_nation = models.CharField(max_length=16, verbose_name='국적')
    user_nickname = models.CharField(max_length=8, unique=True, verbose_name='닉네임')

