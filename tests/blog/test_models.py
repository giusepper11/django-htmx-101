import pytest

#  is a way to apply the @pytest.mark.django_db decorator at the module level in pytest
pytestmark = pytest.mark.django_db


class TestPostModel:

    # @pytest.mark.django_db
    def test_str_return(self, post_factory, user_factory):
        author = user_factory(username="author")
        post = post_factory(title="Post title", author=author)
        assert post.__str__() == "Title: Post title - Author: author"
