"""
Test for models.
"""
from datetime import datetime, timezone

from django.test import TestCase

from core import models


class ModelTests(TestCase):
    """Test models."""

    def test_create_record(self):
        """Test creating a user sucessful."""
        user = models.UserSchema.objects.create(
            first_name='Abdullah',
            last_name='Mujahid',
            email='abdullahmujahidali1@gmail.com',
            hubspot_id='xyzabc',
            created_at=datetime.now(tz=timezone.utc)
        )
        self.assertEqual(str(user), user.first_name + " " + user.last_name)
