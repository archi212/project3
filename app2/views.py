from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def thin(request):
    return HttpResponse("amith")
