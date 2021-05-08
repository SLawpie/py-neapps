from django.urls import path, re_path
from start import views

urlpatterns = [
    path('home/', views.home, name='home'),
    re_path(r'^', views.start, name='start'),
]