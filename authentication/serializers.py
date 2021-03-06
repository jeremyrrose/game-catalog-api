from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import User, UserWatch
from apps.gaming.serializers import GameSerializer, ReviewSerializer


class RegistrationSerializer(serializers.ModelSerializer):
    """Serializers registration requests and creates a new user."""

    password = serializers.CharField(
        max_length=255,
        min_length=8,
        write_only=True
    )
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        # List all of the fields that could possibly be included in a request
        # or response
        fields = ('username', 'email', 'first_name', 'last_name', 'password', 'token')

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    """Serializer login requests and signin user"""
    email = serializers.CharField(max_length=255, read_only=True)
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'token')

    def validate(self, data):
        username = data.get('username', None)
        password = data.get('password', None)

        # Raise an exception if a
        # username is not provided.
        if username is None:
            raise serializers.ValidationError(
                'A username is required to login'
            )
        # Raise an exception if a
        # password is not provided.
        if password is None:
            raise serializers.ValidationError(
                'A password is required to login'
            )
        user = authenticate(username=username, password=password)
        if user is None:
            raise serializers.ValidationError(
                'A user with that username or password was not found'
            )
        if not user.is_active:
            raise serializers.ValidationError(
                'This user has been deactivated'
            )
        return {
            "id": user.pk,
            "username": user.username,
            "email": user.email,
            "token": user.token
        }


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class UserInfoSerializer(serializers.ModelSerializer):
    watch_list = GameSerializer(many=True, required=False)
    games = GameSerializer(many=True, required=False)
    reviews = ReviewSerializer(many=True, required=False)

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'reviews', 'games', 'watch_list', 'platforms',)
        extra_kwargs = {'watch_list': {'required': False}}


class ManyGamesSerializer(serializers.ModelSerializer):
    # user_id = UserInfoSerializer(many=True, required=False)
    game_id = GameSerializer(many=True, required=False)

    class Meta:
        model: UserWatch
        fields = ('id', 'user_id', 'game_id')
