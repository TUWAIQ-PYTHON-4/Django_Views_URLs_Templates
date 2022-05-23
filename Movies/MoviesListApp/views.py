from django.shortcuts import render
# Create your views here.
def index(request):
    return render(request, 'base.html')


def search(request):
    search = request.GET.get('search') or 'empty'
    return  render(request, 'search_result.html', {'search': search})




