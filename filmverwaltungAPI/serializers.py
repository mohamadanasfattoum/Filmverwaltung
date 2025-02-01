from rest_framework import serializers
from .models import Film, Director


class FilmSerializers(serializers.ModelSerializer):
    class Meta:
        model =  Film
        fielde = '__all__'