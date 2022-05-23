from django.shortcuts import render

# Create your views here.
def index(request):
    return  render(request,'base.html')

def search(request):
    name = request.GET.get('name') or 'Search'
    return render(request, 'search.html', {'name': name})