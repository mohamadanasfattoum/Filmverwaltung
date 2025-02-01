from rest_framework import serializers
from .models import Film, Director



class DirectorListSerializers(serializers.ModelSerializer):
    class Meta:
        model =  Director
        fields = '__all__'




class DirectorSerializers(serializers.ModelSerializer):
    class Meta:
        model =  Director
        fields = ['name']



class FilmSerializers(serializers.ModelSerializer):
    director = DirectorSerializers()
    class Meta:
        model =  Film
        fields = '__all__'

    def create(self, validated_data):
        # Extrahiere die Director-Daten
        director_data = validated_data.pop('director')
        # Erstelle oder hole den Director
        director, created = Director.objects.get_or_create(**director_data)
        # Erstelle das Film-Objekt
        film = Film.objects.create(director=director, **validated_data)
        return film

""" Die create()-Methode ermöglicht es dir, komplexe Datenstrukturen zu verarbeiten, indem sie sicherstellt,
dass alle relevanten Objekte (in diesem Fall sowohl Film als auch Director) korrekt erstellt oder zugeordnet werden. """
