from django.urls import path
import MoviesListApp.views

urlpatterns = [
    path('', MoviesListApp.views.Movie_Name)
    ]
