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



