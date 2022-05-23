from django.shortcuts import render

# Create your views here.
def Movie_name(request):

    return render(request, 'base.html')
def IndexView(request):
    search = request.GET.get("search") or "404"
    return render(request, "search.html", {"search": search})
