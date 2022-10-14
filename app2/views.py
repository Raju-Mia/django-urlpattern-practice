from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def myname(request):
    return HttpResponse("this is second app")


def myage(request):
    return HttpResponse("my age 23")


def name(request, name,age):
    return HttpResponse(f"my name is {name} and my age {age}")