# Create your views here.
from django.shortcuts import render


# Create your views here.
def index(request):
    x = 'HELLO'
    return render(request, "index.html", {'x': x})

def Movie_Search(request):
    search = request.GET.get('search') or 33
    return render(request, "search.html", {'search': search})

'''def about(request):
    return render(request, "about.html")'''

