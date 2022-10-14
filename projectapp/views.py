from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def myname(request):
    return HttpResponse("hello world")


def myage(request):
    return HttpResponse("this is first app ... age is 22")