import pytest
from . import models

AUTHOR = "test"
TEXT = "this is txt"
EMAIL = 'testuser@gmail.com'
USERNAME = 'testuser'
PASSWORD = 'testpassowrd'

@pytest.mark.django_db
@pytest.fixture
def message_0():
    return models.Message(
        user=models.User(
            email=EMAIL,
            username=USERNAME,
            password=PASSWORD,
        ),
        author=AUTHOR,
        text=TEXT
    )


@pytest.mark.django_db
class TestMessageModel:
    def test_create_message(self, message_0):
        assert message_0.user.email == EMAIL
        assert message_0.user.username == USERNAME
        assert message_0.user.password == PASSWORD
        assert message_0.author == AUTHOR
        assert message_0.text == TEXT

    def test_persist_member(self, message_0):
        message_0.user.save()
        assert message_0 in models.Message.objects.all()