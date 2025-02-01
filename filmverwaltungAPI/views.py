from django.shortcuts import render
from rest_framework import generics
from .models import Film, Director
from .serializers import FilmSerializers


class FilmsAPIViews(generics.ListCreateAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializers





