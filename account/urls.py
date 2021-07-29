from django.urls import path
from .import views

urlpatterns = [
    path('login/',views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/',views.register, name='register'),
    path('mypageProfile/',views.mypageProfile, name='mypageProfile'),
    path('kakaoLoginLogic/', views.kakaoLoginLogic, name='kakaoLoginLogic'),
    path('kakaoLoginLogicRedirect/', views.kakaoLoginLogicRedirect, name='kakaoLoginLogicRedirect'),
    # path('kakaoLogout/', views.kakaoLogout, name='kakaoLogout'),
]