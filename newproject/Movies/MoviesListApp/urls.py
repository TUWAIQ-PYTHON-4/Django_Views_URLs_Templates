from django.urls import path
import MoviesListApp.views
urlpatterns = [
    path('', MoviesListApp.views.index),
    path('result/', MoviesListApp.views.Movie_Name),
]