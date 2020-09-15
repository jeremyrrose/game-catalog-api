from .models import Game, Platform, Review
from authentication.serializers import UserListSerializer
from rest_framework import serializers


class ReviewSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Review
        fields = ('id', 'owner', 'game', 'header', 'text', 'is_official')


class GameSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, required=False)

    class Meta:
        model = Game
        fields = ('id', 'name', 'platforms', 'region', 'rating',
                  'developers', 'release_date', 'reviews', 'cover', 'banner')


class PlatformSerializer(serializers.ModelSerializer):
    games = GameSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Platform
        fields = ('id', 'name', 'games')
