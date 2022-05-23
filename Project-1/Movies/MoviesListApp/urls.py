from django.urls import path
import MoviesListApp.views
urlpatterns = [
    path('', MoviesListApp.views.index, name='index'),
    path('search/', MoviesListApp.views.search, name='search')
]