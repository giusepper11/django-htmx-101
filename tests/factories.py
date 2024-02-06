import factory
from django.contrib.auth.models import User

from djblogger.blog.models import Post


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker('user_name')
    email = factory.Faker('email')
    password = factory.Faker('password')
    is_superuser = True
    is_staff = True


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    title = factory.Faker('sentence', nb_words=4)
    subtitle = factory.Faker('sentence', nb_words=6)
    slug = ''
    author = factory.SubFactory(UserFactory)
    content = factory.Faker('text')
    status = 'published'
