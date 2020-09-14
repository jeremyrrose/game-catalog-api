from django.db import models
import json
from authentication.models import User


# Create your models here.


class Game(models.Model):
    owner: models.ManyToManyField(User)
    name: models.CharField(max_length=100)
    region: models.CharField(max_length=100)
    rating: models.CharField(max_length=500)
    developers: models.CharField(max_length=500)
    release_date: models.CharField(max_length=50)
    # Image urls for the frontend
    cover: models.TextField()
    banner: models.TextField()

    # Might need to move to serializers
    def set_rating(self, rating, dev):
        self.rating = json.dumps(rating)
        self.developers = json.dumps(dev)


class Review(models.Model):
    game: models.ForeignKey(Game, on_delete=models.CASCADE)
    owner: models.ForeignKey(User, on_delete=models.CASCADE)
    text: models.TextField()
    is_Official: models.BooleanField(default=False)


class Platform(models.Model):
    name = models.CharField(max_length=50)
    # Ask about multiple owners
    games = models.ManyToManyField(Game)
