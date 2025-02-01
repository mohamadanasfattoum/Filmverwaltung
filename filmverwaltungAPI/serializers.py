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
    # director = serializers.StringRelatedField() # anstatt z.22 und 14-17

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

    def update(self, instance, validated_data):
        director_data = validated_data.pop('director', None)

        if director_data:
            director, created = Director.objects.get_or_create(**director_data)
            instance.director = director
        
        instance.title = validated_data.get('title', instance.title)
        instance.genre = validated_data.get('genre', instance.genre)
        instance.release_date = validated_data.get('release_date', instance.release_date)

        instance.save()
        return instance


""" Die create()-Methode ermöglicht es dir, komplexe Datenstrukturen zu verarbeiten, indem sie sicherstellt,
dass alle relevanten Objekte (in diesem Fall sowohl Film als auch Director) korrekt erstellt oder zugeordnet werden. """
