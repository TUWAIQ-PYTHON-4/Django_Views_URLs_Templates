from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
"""def hello(request):
    m = "Hello"
    return HttpResponse(m)"""


# Task one
def index(request):
    x = "Rahaf"
    return render(request, 'base.html', {"x": x})


# Task Two
def movies_search(request):
    name = request.GET.get("name") or "Rahaf"
    return render(request, 'movies-search.html', {"name": name})


"""def name(request):
    x = request.GET.get("Rahaf")
    return HttpResponse("Hello {}".format(x))"""
