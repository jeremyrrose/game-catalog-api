# Game Catalog API
Forked from [Ebs B.'s Recreation API](https://github.com/e-mbrown/p4-backend). 

Deployed at https://game-catalog-django.herokuapp.com/



## Overview

This API is built for a gaming Ecommerce site that takes inspiration from pre-existing sites such as the Origin. Recreation Api uses the Django rest framework. Originally I was going to use an external api to hold the game information and my api would hold relationships, but decidded to seed a couple of games instead

Authentication models- Users, Login
Gaming Models - Platform, Developer, Game(connected to Platform, User, and Developer), and Review(connected to Game and User)

## Key Models
```python
User:
    username = models.CharField(db_index=True, max_length=255, unique=True)
    email = models.EmailField(db_index=True, unique=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    games = models.ManyToManyField(Game, default=None, blank=True, related_name='owned')
    watch_list = models.ManyToManyField(Game, default=None, blank=True, related_name='watcher')
    platforms = models.ManyToManyField(Platform)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```
```python
Game:
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
```

## Key Endpoints
```
Auth:
auth/users/register/      POST
auth/users/login/         POST
auth/users/               GET
auth/many/:user_id/       GET, PATCH, PUT (patch recommended)
```
```Gaming API:
gaming/games/             GET, POST
gaming/games/:game_id/    GET, PUT, DELETE
gaming/reviews/           GET, POST
gaming/reviews/:review_id/   GET, PUT, DELETE
```

