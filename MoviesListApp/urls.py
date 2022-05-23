
from django.urls import path
import MoviesListApp.views
urlpatterns = [path('', MoviesListApp.views.index, name='index'),
               path('Movie_name/', MoviesListApp.views.Movie_name, name='Movie_name')
               ]