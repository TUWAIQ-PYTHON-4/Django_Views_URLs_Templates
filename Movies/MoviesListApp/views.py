
def index(request):
    return render(request,"base.html")
def Movie_Name(request):
    name= request.GET.get("name")
    return render(request,'result.html',{"name":name})
