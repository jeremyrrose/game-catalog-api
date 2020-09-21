from django.shortcuts import render
from .models import Game, Platform, Review, Developer
from django.http import HttpResponse
from authentication.models import User
from rest_framework import viewsets, permissions
from .serializers import GameSerializer, PlatformSerializer, ReviewSerializer, DeveloperSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.exceptions import (
    ValidationError, PermissionDenied
)
from rest_framework import generics


# Create your views here.

class GameViewSet(generics.ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = GameSerializer

    def get_queryset(self):
            queryset = Game.objects.all()
            return queryset


class OneGameViewSet(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (AllowAny,)
    serializer_class = GameSerializer

    def get_queryset(self):
        if self.kwargs.get('pk'):
            game = Game.objects.filter(pk=self.kwargs['pk'])
            queryset = game
            return queryset


class DeveloperViewset(generics.ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = DeveloperSerializer
    def get_queryset(self):
            queryset = Developer.objects.all()
            return queryset


class PlatformViewSet(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = PlatformSerializer

    def get_queryset(self):
        if self.kwargs.get('pk'):
            platform = Platform.objects.get(pk=self.kwargs['pk'])
            queryset = platform
            print(queryset)
            return queryset


class ReviewViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ReviewSerializer

    def get_queryset(self):
        queryset = Review.objects.all()
        return queryset

    def create(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            raise PermissionDenied(
                "Seems like you aren't logged in, that's a shame."
            )
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def destroy(self, request, *args, **kwargs):
        review = Review.objects.get(pk=self.kwargs['pk'])
        if not request.user == review.owner:
            raise PermissionDenied(
                "This isn't your review, you dont have the power to delete it"
            )
        return super().destroy(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        review = Review.objects.get(pk=self.kwargs['pk'])
        if not request.user == review.owner:
            raise PermissionDenied(
                "You can't rearrange the words of other people!!"
            )
        return super().update(request, *args, **kwargs)

