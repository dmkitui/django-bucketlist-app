from django.test import TestCase
from ..models import Bucketlists


class ModelTestCase(TestCase):
    """Tests for the bucketlist model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.bucketlist_name = "Make the world a better place"
        self.bucketlist = Bucketlists(name=self.bucketlist_name)

    def test_can_create_a_bucketlist(self):
        """Test the creation of a new bucketlist."""
        current_count = Bucketlists.objects.count()
        self.bucketlist.save()
        new_count = Bucketlists.objects.count()
        self.assertNotEqual(current_count, new_count)


