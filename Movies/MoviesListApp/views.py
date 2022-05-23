from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, "base.html")

def about(request):
    return render(request, 'about.html')

def product(request):
    return render(request, 'product.html')

def MovieSearch(request):
    return render(request, 'SearchResult.html')

def SearchResult(request):
    name = request.GET.get("name") or "Michal"
    return render(request, "SearchResult.html", {"name": name})
