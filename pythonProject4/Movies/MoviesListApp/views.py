from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, "base.html")


def search(request):
    name = request.GET.get("name") or "Harry Potter"
    return render(request, "movies-search.html", {"name": name})
