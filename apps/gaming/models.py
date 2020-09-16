from django.db import models


# import json


# Create your models here.


class Platform(models.Model):
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=55)

    def __str__(self):
        return self.name

class Developer(models.Model):
    name = models.CharField(max_length=100)


class Game(models.Model):
    name = models.CharField(max_length=100, default=None)
    region = models.CharField(max_length=100, default=None)
    rating = models.CharField(max_length=500, default=None)
    developers = models.ManyToManyField(Developer, default=None, related_name='developers')
    description = models.TextField(default=None)
    # Many to Many is a django field, it does a thing. I think it makes a table thing
    platforms = models.ManyToManyField(Platform, default=None, related_name='games')
    release_date = models.DateTimeField(default=None)
    # Image urls for the frontend
    cover = models.TextField(default=None)
    banner = models.TextField(default=None)

    def __str__(self):
        return self.name


    # Might need to move to views ??
    # def set_rating(self, dev):
    #     self.developers = json.dumps(dev)


class Review(models.Model):
    header = models.CharField(max_length=100, default=None)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, default=None, related_name='reviews')
    owner = models.ForeignKey('authentication.User', on_delete=models.CASCADE)
    text = models.TextField(default=None)
    is_official = models.BooleanField(default=False)

    def __str__(self):
        return self.header
