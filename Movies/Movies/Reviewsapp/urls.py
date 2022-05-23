# from django.contrib import admin
from django.urls import path
import Reviewsapp.views

urlpatterns = [
    path('', Reviewsapp.views.index),
    path('search/', Reviewsapp.views.search)
    ]
