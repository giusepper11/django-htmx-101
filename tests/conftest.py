from pytest_factoryboy import register

from .factories import PostFactory, UserFactory

a = register(UserFactory)
b = register(PostFactory)
