from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.

def myfunctionCall(request):
    return HttpResponse("Hello World")


def myfunctionAbout(request):
    return HttpResponse("About Page")
