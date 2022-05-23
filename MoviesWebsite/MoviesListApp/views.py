from django.shortcuts import render


def index_view(request):
    return render(request, "base.html")


def search(request):
    search_word = request.GET.get("search_word") or "Harry potter"
    return render(request, "search.html", {"search_word": search_word})
