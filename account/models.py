from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser
# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, password):
        user = self.create_user(
            email,
            password=password,
            date_of_birth=date_of_birth,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractUser):
    user_name = models.CharField(max_length=16,  verbose_name='이름')
    user_gender = models.CharField(max_length=8, verbose_name='성별')
    user_nation = models.CharField(max_length=16, verbose_name='국적')
    user_nickname = models.CharField(max_length=8, unique=True, verbose_name='닉네임')
    kakao_id = models.CharField(max_length=200, unique=True, verbose_name='카카오 아이디', default=0)

