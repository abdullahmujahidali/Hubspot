# Standard Library
from uuid import uuid4

# Django
from django.utils.translation import gettext_lazy as _
from django.db import models

# Create your models here.


class UserSchema(models.Model):
    """User object."""
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField()
    hubspot_id = models.CharField(max_length=80, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "abdullah-Contact"
        verbose_name = _("Abdullah-Contact")
        verbose_name_plural = _("Abdullah-Contact")
        ordering = [
            "-created_at",
        ]

    def __str__(self):
        return self.first_name + " " + self.last_name
