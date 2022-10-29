from rest_framework import generics

from core.mixins import PublicViewMixin
from .serializers import UserSerializer


class API(PublicViewMixin, generics.CreateAPIView):
    """This api will allow user to create a model instance into the database."""

    serializer_class = UserSerializer
