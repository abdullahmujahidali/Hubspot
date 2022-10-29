import requests
import json
# DRF
from rest_framework import serializers

# 3rd Party Libraries
from core.models import UserSchema


class UserSerializer(serializers.ModelSerializer):
    """This serializer is used to list all the notifications for a user."""

    class Meta:
        model = UserSchema
        fields = ("first_name", "last_name", "email", "hubspot_id")

    def create(self, validated_data):
        res = requests.post(
            "https://api.hubapi.com/contacts/v1/contact/pat-na1-ba52c54e-b47c-416a-88d3-1ba19d5dcacb",
            headers={},
            data=json.dumps(
                {
                    "properties": [
                        {"property": "email",
                         "value": validated_data["email"]},
                        {"property": "firstname",
                         "value": validated_data["first_name"]},
                        {"property": "lastname",
                         "value": validated_data["last_name"]},
                    ]
                }
            ),
        )
        print("res: ", res)
        print("VALIDATED_DAA: ", validated_data)
        return res
