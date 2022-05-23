from django.urls import path
from . import views

urlpatterns = [
    path('', views.Movie_Name, name='Movie_Name'),
    path('about/', views.about, name='about')]
