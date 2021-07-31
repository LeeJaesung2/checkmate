from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser



class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields+('user_name','user_gender','user_nation','user_nickname','kakao_id')

