# Create your views here.
from django.shortcuts import render


# Create your views here.
def index(request):
    message = "...."
    x = 'HELLO'
    return render(request, "base.html", {'x': x})

def Movie_Search(request):
    message = "...."
    search = request.GET.get('search') or 33
    return render(request, "base.html", { 'search': search})

def about(request):
    return render(request, "about.html")
