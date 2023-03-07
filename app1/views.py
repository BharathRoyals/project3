from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def app1(request):
    return HttpResponse('<h1><marquee>this is my new app</marquee></h1>')