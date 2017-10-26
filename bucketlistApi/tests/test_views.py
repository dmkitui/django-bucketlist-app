from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse
from django.test import TestCase
from ..models import Bucketlists
from django.contrib.auth.models import User


class ViewTestCase(TestCase):
    """Tests for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        owner = User.objects.create(username='OptimusPrime')
        self.client.force_authenticate(user=owner)
        self.bucketlist_data = {'name': 'Travel the world', 'owner': owner.id}
        self.response = self.client.post(reverse('create'), self.bucketlist_data, format="json")

    def test_api_can_create_a_bucketlist(self):
        """Test the api can create a bucketlist."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_bucketlist(self):
        """Test the api get a specified bucketlist."""
        bucketlist = Bucketlists.objects.get(id=1)
        response = self.client.get(
            reverse('details', kwargs={'pk': bucketlist.id}), format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, bucketlist)

    def test_api_can_delete_bucketlist(self):
        """Test can delete a specified bucketlist."""
        bucketlists = Bucketlists.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk': bucketlists.id}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_api_can_update_bucketlist(self):
        """Test can update a specified bucketlist."""
        bucketlists = Bucketlists.objects.get()
        change_bucketlist = {'name': 'Travel the whole world...'}
        res = self.client.put(
            reverse('details', kwargs={'pk': bucketlists.id}),
            change_bucketlist, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_authorization(self):
        """Test that the api enforces user authorization."""
        fresh_client = APIClient()
        # Use a user id for a use that does not exist.
        res = fresh_client.get('/bucketlists/', kwargs={'pk': 801}, format="json")
        print('RES: ', res)
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)
