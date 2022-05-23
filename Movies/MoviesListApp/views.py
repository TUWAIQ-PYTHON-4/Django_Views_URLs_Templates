# Create your views here.
from django.shortcuts import render


# Create your views here.
def Movie_Name(request):
    message = "...."
    x = 'HELLO'
    page = request.GET.get('page') or 33
    return render(request, "base.html", {'x': x, 'page': page})


def about(request):
    return render(request, "about.html")
