from django.urls import path
from .import views

urlpatterns = [
    path('searchRoommate/',views.searchRoommate, name='searchRoommate'),
    path('detail/<int:write_id>', views.detail, name='detail'),
    path('create',views.create, name='create'),
    path('update/<int:write_id>', views.update, name='update'),
    path('delete/<int:write_id>', views.delete, name='delete'),
    path('commnet_action/<int:write_id>/', views.commnet_action, name='commnet_action')
]