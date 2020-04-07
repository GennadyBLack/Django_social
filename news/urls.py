from django.urls import path
from .views import *
urlpatterns = [
    path('',news_list,name='news_list'),
    path('create/',news_create,name='news_create'),
    path('<int:id>',news_detail,name='news_detail'),
    path('review/',add_review, name='add_review')

]
