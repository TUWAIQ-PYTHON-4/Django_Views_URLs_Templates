from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def index(request):
    return render(request , "base.html")

def movie_search(request):
    name = request.GET.get("name") or "Nothing"
    return render(request, "search_result.html", {"name": name})