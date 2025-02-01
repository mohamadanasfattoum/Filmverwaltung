from django.urls import path
from .views import FilmsAPIViews, DirectorAPIViews

urlpatterns = [
    path("films/", FilmsAPIViews.as_view(), name="films"),
    path("directors/", DirectorAPIViews.as_view(), name=" directors"),

 ]
