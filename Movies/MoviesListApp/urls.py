
import MoviesListApp.views
from django.urls import path

urlpatterns = {

    path('', MoviesListApp.views.index),
    path('SearchResult/', MoviesListApp.views.SearchResult)
}