from django.urls import path
from .import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('login/',views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/',views.register, name='register'),
    path('kakaoLoginLogic/', views.kakaoLoginLogic, name='kakaoLoginLogic'),
    path('kakaoLoginLogicRedirect/', views.kakaoLoginLogicRedirect, name='kakaoLoginLogicRedirect'),
    path('mypageProfile/', views.mypageProfile, name='mypageProfile'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)