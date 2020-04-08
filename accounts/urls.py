from django.urls import path
from .views import *

urlpatterns = [
 path('<int:id>/edit_profile_news/',edit_profile_news,name='edit_profile_news'),
    path('login/',login,name='login'),
    path('register/',register,name='register'),
    path('logout/',logout,name='logout'),
    path('dashboard',dashboard,name='dashboard'),
    path('edit_profile/',edit_profile,name='edit_profile'),
    path('profile_list/',profile_list,name='profile_list'),
    path('profile_list/search/',profile_list_search,name='profile_list_search'),
]
