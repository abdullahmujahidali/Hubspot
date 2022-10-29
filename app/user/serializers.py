import json
from urllib import request
import requests
# DRF
from rest_framework import serializers

# 3rd Party Libraries
from core.models import UserSchema

class UserSerializer(serializers.ModelSerializer):
    """This serializer is used serialize user info and create an account on hubspot and in database."""

    class Meta:
        model = UserSchema
        fields = ["first_name", "last_name", "email"]

    def create(self, validated_data):
        # resp = requests.post(
        #     "https://api.hubapi.com/oauth/v1/token",
        #     headers={
        #         'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8'},
        #     data={
        #         'grant_type':'authorization_code',
        #         'client_id':'a3854853-aec0-4522-aaad-a6270161d187',
        #         'client_secret':'f140377b-2231-4fe8-88e5-8704d4fd24e3', 
        #         'redirect_uri': 'https://google.com/',
        #         'code':'854ce293-a00e-4f4b-b64b-43f65cd4170c',
        #     }
        # )
        # print('res: ', resp.content)

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
