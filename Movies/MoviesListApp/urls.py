from django.urls import path
import MoviesListApp.views

from . import views
urlpatterns = [
    path('', views.Movie_Name, name='Movie_Name')]