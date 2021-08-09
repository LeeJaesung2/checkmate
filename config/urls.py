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
from checkmate import views

from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.conf.urls import url


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main ,name='main'),
    path('infoWrite/', views.infoWrite, name='infoWrite'),
    path('dom_infoWrite/', views.dom_infoWrite, name='dom_infoWrite'),
    path('account/', include('account.urls')),
    path('survey/', include('survey.urls')),
    path('roommate/', include('roommate.urls')),
    path('chat/', include('chat.urls')),
    path('mypageScrap/',views.mypageScrap, name='mypageScrap'),
    path('mypageWritten/',views.mypageWritten, name='mypageWritten'),
    path('offcampusCommunity/',views.offcampusCommunity, name='offcampusCommunity'),
    path('domitoryCommunity/',views.domitoryCommunity, name='domitoryCommunity'),
    path('offcampusView/<int:post_id>',views.offcampusView, name='offcampusView'),
    path('domitoryView/<int:post_id>',views.domitoryView, name='domitoryView'),
    path('offcampusDelete/<int:post_id>',views.offcampusDelete, name='offcampusDelete'),
    path('domitoryDelete/<int:post_id>',views.domitoryDelete, name='domitoryDelete'),
    path('offcampusUpdate/<int:post_id>',views.offcampusUpdate, name='offcampusUpdate'),
    path('domitoryUpdate/<int:post_id>',views.domitoryUpdate, name='domitoryUpdate'),
    path('domitory_scrap/<int:post_id>',views.domitory_scrap, name='domitory_scrap'),
    path('offcampus_scrap/<int:post_id>',views.offcampus_scrap, name='offcampus_scrap'),
    url(r'^media/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT,})



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
