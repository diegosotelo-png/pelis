from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=200)
    synopsis = models.TextField()
    duracion_minutos = models.IntegerField()

    Director = models.CharField(max_length=150, null=True, blank=True)  # NUEVO

    genres = models.ManyToManyField(Genre, related_name='movies')

    def __str__(self):
        return self.title