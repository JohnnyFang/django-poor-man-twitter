import pytest
from django.test import Client

pytestmark = pytest.mark.django_db

class TestTweetViewSet:

    def test(self):
        client = Client()
        response = client.get("")
        assert response.status_code == 200