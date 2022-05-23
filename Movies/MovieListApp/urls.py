from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('movies-search/', views.search, name='search'),
]