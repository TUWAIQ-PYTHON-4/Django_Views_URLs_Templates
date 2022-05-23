from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse
from django.shortcuts import render


def index_view(request):
    return render(request, 'base.html')


def movies_search(request):
    name = request.GET.get('name')
    return render(request, 'search.html', {'name': name})
