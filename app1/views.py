from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('Home')
# Create your views here.
def myfun(request):
    return HttpResponse("Hello, Arvind!")