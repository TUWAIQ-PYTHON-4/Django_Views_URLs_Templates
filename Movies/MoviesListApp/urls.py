from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index')
    ,path('search_result/', views.search, name = 'search')
    ]
