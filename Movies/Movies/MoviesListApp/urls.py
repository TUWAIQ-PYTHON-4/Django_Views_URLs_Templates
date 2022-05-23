from django.urls import path
import MoviesListApp.views

urlpatterns = [path('', MoviesListApp.views.Movie_Name, name='Movie_Name'),
               path('s/', MoviesListApp.views.search, name='name')
               ]

