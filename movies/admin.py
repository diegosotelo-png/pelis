from django.contrib import admin
from .models import Movie, Genre

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    search_fields = ['name']  # IMPORTANTE


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'duracion_minutos')

    autocomplete_fields = ['genres']  # 🔥 MEJOR OPCIÓN