# Django
from django.urls import path


from user.views import API

app_name = "user"

urlpatterns = [
    path("create/", API.as_view(), name="create-account"),
]
