from django.db import models
from account.models import CustomUser

# Create your models here.

class Write(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()

    state_choice = (
        ('매칭중', '매칭중'), 
        ('매칭완료', '매칭완료'),
        )
    state = models.CharField(max_length=4, choices=state_choice, default='매칭중')

    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)


    def __str__(self):
        return self.title