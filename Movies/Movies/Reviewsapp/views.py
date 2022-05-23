from django.shortcuts import render

# Create your views here.

def index(request):
    # page = request.GET.get('page') or "Harry Potter" # ? = 6
    return render(request, "base.html")

def search(request):
    search = request.GET.get('search') or "Harry Potter"
    return render(request,"movies-search.html",{'search':search})
