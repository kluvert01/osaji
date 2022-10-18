from . import views

from django.urls import path


urlpatterns = [
    path("", views.index, name="index"),
    path("hello", views.welcome, name="play"),
    path("blog/", views.blog, name="ply")
]