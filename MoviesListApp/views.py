
from django.shortcuts import render
def index(request):
        value_search= " in My page"
        page=request.GET.get("page") or "Lab 1"
        return render(request, "searchresult.html",{"value_search":value_search , "page":page})

