from django.shortcuts import render


def Movie_name(request):

    return render(request, "base.html")


def search_result(request):
    page = request.GET.get("page") or "22"
    return render(request, "search_result.html", {"page": page})