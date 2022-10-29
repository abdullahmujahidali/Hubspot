# DRF
from rest_framework.permissions import AllowAny


class PublicViewMixin:
    """This mixin is used to make any view public. That means it
        removes authentication and permission from view."""

    authentication_classes = ()
    permission_classes = (AllowAny,)
