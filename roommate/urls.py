from django.urls import path
from .import views

urlpatterns = [
    path('searchRoommate/',views.searchRoommate, name='searchRoommate'),
    path('detail/',views.detail, name='detail'),
]