from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#def home(request):
#    return HttpResponse('Home Page of App1')


def home(request):
    return render(request,'app1/home.html')