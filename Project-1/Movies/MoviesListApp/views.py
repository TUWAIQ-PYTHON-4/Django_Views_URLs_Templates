from django.shortcuts import render

def index(request):
    return render(request,"base.html")

def search(request):
    search = request.GET.get("search") or "Harry Potter"
    return render(request,"sch.html",{'search':search})