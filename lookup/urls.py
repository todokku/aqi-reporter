# This urls.py is accessed by the weather/urls.py 
from django.urls import path
from . import views # . stands for this directory aka lookup

urlpatterns = [
    path('', views.home, name="home"),
    path('about.html', views.about, name="about"),
]
