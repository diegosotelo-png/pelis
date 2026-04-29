import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from movies.models import Movie
from reviews.models import Review
import random

movies = Movie.objects.all()

authors = ["Diego", "Ana", "Luis", "Carlos", "Maria"]

for i in range(20):
    Review.objects.create(
        movie=random.choice(movies),
        author=random.choice(authors),
        comment="Muy buena película",
        rating=random.randint(6, 10)
    )

print("Datos insertados")