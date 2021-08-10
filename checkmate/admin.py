from django.contrib import admin
from checkmate.models import Offcampus_Post,Domitory_Post, Scrap_roommate, Scrap_dom, Scrap_off

# Register your models here.
admin.site.register(Offcampus_Post)
admin.site.register(Domitory_Post)
admin.site.register(Scrap_roommate)
admin.site.register(Scrap_dom)
admin.site.register(Scrap_off)