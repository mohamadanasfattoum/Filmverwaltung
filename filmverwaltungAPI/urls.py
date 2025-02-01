from django.urls import path
from .views import FilmsAPIViews, DirectorAPIViews, FilmRetrieveAPIViews, DirectorRetrieveAPIViews

urlpatterns = [
    path("films/", FilmsAPIViews.as_view(), name="films"),
    path("directors/", DirectorAPIViews.as_view(), name=" directors"),
    path("films/<int:pk>", FilmRetrieveAPIViews.as_view()),
    path("directors/<int:pk>", DirectorRetrieveAPIViews.as_view()),

 ]
