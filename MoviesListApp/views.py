
from django.shortcuts import render
def index(request):
        return render(request, "base.html")

def Movie_name(request):
        value_search = " Lion King"
        page = request.GET.get("page") or "Lab 1"
        return render(request, "searchresult.html", {"value_search": value_search, "page": page})