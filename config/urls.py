"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
from django.contrib import admin
from django.urls import path, include
from survey import views
from checkmate import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main ,name='main'),
    path('infoWrite/', views.infoWrite, name='infoWrite'),
    path('account/', include('account.urls')),
    path('survey/', views.survey, name='survey'),
    path('mypageScrap/',views.mypageScrap, name='mypageScrap'),
    path('mypageWritten/',views.mypageWritten, name='mypageWritten'),
    path('searchRoommate/',views.searchRoommate, name='searchRoommate'),
    path('detail/',views.detail, name='detail'),
    path('community/',views.community, name='community'),
]
