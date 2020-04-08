from django.urls import path
from .views import *
urlpatterns = [
    path('',room_list,name='room_list'),
    path('create/',room_create,name='room_create'),
    path('<int:id>',room_detail,name='room_detail'),
    path('home/',index,name='index'),
    path('about/',about,name='about'),




    #API path

]
