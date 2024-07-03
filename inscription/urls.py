from django.urls import path
from django.contrib.sitemaps.views import sitemap

from .views import *



app_name = "inscription"
urlpatterns = [
    path("", index, name="index"),

]