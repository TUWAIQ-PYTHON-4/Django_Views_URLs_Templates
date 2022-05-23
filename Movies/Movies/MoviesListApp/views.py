from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def Movie_Name(request):
    return HttpResponse("This page displays information about the movies")

