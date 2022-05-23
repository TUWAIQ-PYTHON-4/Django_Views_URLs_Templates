
from django.contrib import admin
from django.urls import path
import MoviesList.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MoviesList.views.IndexView),

]
