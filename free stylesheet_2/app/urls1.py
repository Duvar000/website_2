from django.contrib import admin
from django.urls import path,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import blog_main

urlpatterns = [
    path("", blog_main.as_view() , name = "blogpage")
]
