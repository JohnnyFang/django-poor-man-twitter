import pytest

from twitter_app.models import Tweet
from twitter_app.serializers import TweetSerializer

pytestmark = pytest.mark.django_db


class TestTweetSerializer:
    """Test TweetSerializer"""
    def test_content(self):
        tweet = Tweet.objects.create(name='johnny', message='This is my test')
        serializer = TweetSerializer(instance=tweet)

        data = serializer.data

        # self.assertEqual(set(data.keys()), set(['color', 'size']))
        assert set(data.keys()) == set(['id', 'message', 'timestamp', 'name'])
