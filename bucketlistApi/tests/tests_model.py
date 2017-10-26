from django.test import TestCase
from ..models import Bucketlists
from django.contrib.auth.models import User


class ModelTestCase(TestCase):
    """Tests for the bucketlist model."""

    def setUp(self):
        """Define the test client and other test variables."""
        current_user = User.objects.create(username="OptimusPrime")
        self.bucketlist_name = 'Make the world a better place'
        self.bucketlist = Bucketlists(name=self.bucketlist_name, owner=current_user)

    def test_can_create_a_bucketlist(self):
        """Test the creation of a new bucketlist."""
        current_count = Bucketlists.objects.count()
        self.bucketlist.save()
        new_count = Bucketlists.objects.count()
        self.assertNotEqual(current_count, new_count)



