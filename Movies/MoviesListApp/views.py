from django.http import HttpResponse
from django.shortcuts import render



# Create your views here.
def Index_viwes(request):
    return render(request,"base.html",)

def Search(request):
    word= request.GET.get('word')
    return render(request,"movies-search.html",{'word':word})
