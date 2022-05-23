from django.shortcuts import render


def Movie_Name(request):
    return render(request, "base.html")


def search(request):
    name = request.GET.get("name") or "Harry Potter"
    return render(request, "search.html", {"name": name})
