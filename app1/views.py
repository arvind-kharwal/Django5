from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h2>Home</h2>')
# Create your views here.
def myfun(request):
    return HttpResponse("Hello, Arvind!")

def math(request):
    l = 10+20
    return HttpResponse('The sum is {}'.format(l))