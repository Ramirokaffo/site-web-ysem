from django.urls import path
from django.contrib.sitemaps.views import sitemap

from .views import index



app_name = "student"
urlpatterns = [
    path("", index, name="index"),
    # path("comment/<int:post_id>/", comment, name="comment"),

]