
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search_result/', views.search_movies, name='index')
]