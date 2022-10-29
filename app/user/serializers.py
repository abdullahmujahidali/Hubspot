import json
import requests
# DRF
from rest_framework import serializers

# 3rd Party Libraries
from core.models import UserSchema

class UserSerializer(serializers.ModelSerializer):
    """This serializer is used serialize user info and create an account on hubspot and in database."""

    class Meta:
        model = UserSchema
        fields = ["first_name", "last_name", "email", "hubspot_id"]

    def create(self, validated_data):
        res = requests.post(
            "https://api.hubapi.com/contacts/v1/contact/",
            headers={
                'Authorization': 'Bearer pat-na1-ba52c54e-b47c-416a-88d3-1ba19d5dcacb',
                'Content-Type': 'application/json'
            },
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
        output = json.loads(res.content)
        UserSchema.objects.create(
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            email=validated_data["email"],
            hubspot_id=output["identityProfile"]["vid"]
        )
        return validated_data
