from django.urls import path
from .import views

from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.conf.urls import url

urlpatterns = [
    path('login/',views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/',views.register, name='register'),
    path('kakaoLoginLogic/', views.kakaoLoginLogic, name='kakaoLoginLogic'),
    path('kakaoLoginLogicRedirect/', views.kakaoLoginLogicRedirect, name='kakaoLoginLogicRedirect'),
    path('mypageProfile/', views.mypageProfile, name='mypageProfile'),
    url(r'^media/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT,})
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)