from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'base.html')

def search_movies(request):
    page = request.GET.get('page')
    return render(request, 'search_result.html', {'page': page})