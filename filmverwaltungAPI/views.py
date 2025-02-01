from django.shortcuts import render
from rest_framework import generics
from .models import Film, Director
from .serializers import FilmSerializers, DirectorListSerializers


class FilmsAPIViews(generics.ListCreateAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializers


class DirectorAPIViews(generics.ListCreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorListSerializers





