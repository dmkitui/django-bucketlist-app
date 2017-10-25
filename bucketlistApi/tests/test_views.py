from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse
from django.test import TestCase


class ViewTestCase(TestCase):
    """Tests for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.bucketlist_data = {'name': 'Travel the world'}
        self.response = self.client.post(
            reverse('create'),
            self.bucketlist_data,
            format="json")

    def test_api_can_create_a_bucketlist(self):
        """Test the api can create a bucketlist."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)