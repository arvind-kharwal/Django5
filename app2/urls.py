from django.urls import path,include
from app2 import views

urlpatterns = [
    path('app2fun/',views.app2fun,name='App 2 Fun'),  
    path('fastapi/',views.fastapi,name='Fastapi'),   
]
