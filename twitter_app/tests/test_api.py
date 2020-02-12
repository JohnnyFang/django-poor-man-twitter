import pytest
import json

from django.test import Client
from rest_framework import status

from twitter_app.models import Tweet

pytestmark = pytest.mark.django_db

class TestApi:
    # endpoints api/tweet/ [GET, POST]

    client = Client()
    invalid_payload = {
        'name': 'Muffin',
        'age': 4,
        'breed': 'Pamerion',
        'color': 'White'
    }
    valid_payload = {
        'name': 'johnny',
        'message': 'This is my test'
    }

    def test_post_valid(self):
        response = self.client.post(
            '/api/tweet/',
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        assert response.status_code == status.HTTP_201_CREATED

    def test_post_invalid(self):
        response = self.client.post(
            '/api/tweet/',
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_get(self):
        Tweet.objects.create(name='johnny', message='This is my test')
        response = self.client.get('/api/tweet/')
        assert len(response.data) == 1
        response_dict = response.data[0]
        assert response_dict['name'] == 'johnny'
        assert response_dict['message'] == 'This is my test'