from django.urls import path
import MoviesListApp.views

from . import views
urlpatterns = [
    path('', views.index, name='index')]