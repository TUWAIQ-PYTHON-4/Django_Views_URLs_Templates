from django.shortcuts import render


from django.shortcuts import render


def index(request):
    return render(request, "base.html")


def Movie_Name(request):
    name = request.GET.get("name")   or "Harry Potter"
    return render(request, 'result.html', {"name": name})
