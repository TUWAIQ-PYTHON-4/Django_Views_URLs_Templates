
# Create your views here.
from django.shortcuts import render

# Create your views here.
def index(request):
    message = "...."
    return render(request, "base.html")