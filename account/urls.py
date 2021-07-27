from django.urls import path
from .import views

urlpatterns = [
    path('login/',views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/',views.register, name='register'),
<<<<<<< HEAD
    path('change_password/',views.change_password, name='change_password'),
=======
    path('kakaoLoginLogic/', views.kakaoLoginLogic, name='kakaoLoginLogic'),
    path('kakaoLoginLogicRedirect/', views.kakaoLoginLogicRedirect, name='kakaoLoginLogicRedirect'),
    path('kakaoLogout/', views.kakaoLogout, name='kakaoLogout'),
>>>>>>> 594a70ea697ec6f073db53a2fd57dfb6a17d3393
]