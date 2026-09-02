from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name="index.html"),
    path('contact', views.contact,name="contact.html"),
    path('about', views.about,name="about.html"),
    path('new', views.new,name="new.html"),
    path('single', views.single,name="single.html"),
    path('specials', views.specials,name="specials.html"),
]