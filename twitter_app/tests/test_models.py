import pytest

from twitter_app.models import Tweet

pytestmark = pytest.mark.django_db

class TestTweet:
    """Test Tweet model"""

    def test_model(self):
        obj = Tweet.objects.create(name='johnny', message='This is my test')
        assert Tweet.objects.count() == 1, 'Should create a Tweet instance'
        assert obj.name == 'johnny', 'Should equal the name given'
