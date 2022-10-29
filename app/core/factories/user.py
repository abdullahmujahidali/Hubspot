# 3rd Party Libraries
import factory
from faker import Factory

# Backend Apps
from core.models import UserSchema

faker = Factory.create()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = UserSchema
    email = factory.LazyAttribute(lambda _: faker.ascii_company_email())
    first_name = factory.LazyAttribute(lambda _: faker.first_name())
    last_name = factory.LazyAttribute(lambda _: faker.last_name())
