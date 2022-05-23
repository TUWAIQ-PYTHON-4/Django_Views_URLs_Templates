from django.urls import path

import MoviesListApp.views

urlpatterns = [
    path('',MoviesListApp.views.index , name ='index'),
    path('movie_search/', MoviesListApp.views.movie_search,name='movie_search')
]