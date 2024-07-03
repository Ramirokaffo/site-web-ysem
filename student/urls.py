from django.urls import path
from django.contrib.sitemaps.views import sitemap

from .views import *



app_name = "student"
urlpatterns = [
    path("", index, name="index"),
    path("course", course, name="course"),
    path("lecturer", lecturer, name="lecturer"),
    path("mark", mark, name="mark"),
    path("preference", preference, name="preference"),

]