from django.db import models


# Film (Titel, Genre, Veröffentlichungsdatum, Regisseur)
# Regisseur (Name, Geburtsdatum, Nationalität)

class Director(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    nationality = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    



class Film(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=50)
    release_date = models.DateField()
    director = models.ForeignKey(Director, related_name='films', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title
