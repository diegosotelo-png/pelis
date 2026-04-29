from rest_framework import serializers
from .models import Movie, Genre
from reviews.models import Review  # NUEVO

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):  # NUEVO
    class Meta:
        model = Review
        fields = ('id', 'author', 'rating', 'comment', 'created_at')


class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)  # 🔥 NUEVO

    class Meta:
        model = Movie
        fields = '__all__'