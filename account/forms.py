from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

from django.contrib.auth.forms import AuthenticationForm

# class CustomAuthenticationForm(AuthenticationForm):
#     error_messages = {
#         'invalid_login': (
#             "비밀번호나 이메일이 올바르지 않습니다. 다시 확인해 주세요."
#         ),
#         'inactive': ("이 계정은 인증되지 않았습니다. 인증을 먼저 진행해 주세요."),
#     }
#     def __init__(self, request=None, *args, **kwargs):
#         super(CustomAuthenticationForm, self).__init__(*args, **kwargs) # 꼭 있어야 한다!
#         self.fields['username'].label = '아이디'
#         self.fields['password'].label = '비밀번호'       

class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields+('user_gender','user_nation','user_nickname')