from django.shortcuts import render

from rest_framework import generics

from core.mixins import PublicViewMixin

# Create your views here.


class API(PublicViewMixin, generics.CreateAPIView):
    """This api will allow user to create a model instance into the database."""

    # serializer_class = serializers.RecipeDetailSerializer
