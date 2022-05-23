from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index_view, name='index_view'),
    path('search/', views.search, name='search')
]