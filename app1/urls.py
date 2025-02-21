from django.urls import path
from app1 import views

urlpatterns = [
    path('', views.blog,name='blog'),
    path('math/', views.math,name='math'),
    path('myfun/', views.myfun,name='myfun'),
    path('home/', views.home,name='home'),
    
]