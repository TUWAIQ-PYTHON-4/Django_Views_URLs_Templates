from django.urls import path
import MoviesListApp.views


urlpatterns = [
    path('', MoviesListApp.views.Movie_name),
    path('search/', MoviesListApp.views.search_result)
]