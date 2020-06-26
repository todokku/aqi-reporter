from django.urls import path
from . import views # . stands for this directory aka lookup

urlpatterns = [
    path('', views.home, name="home"),
    path('about.html', views.about, name="about"),
]
