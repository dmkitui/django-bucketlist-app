from django.test import TestCase
from ..models import Bucketlists, User


class ModelTestCase(TestCase):
    """Tests for the bucketlist model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.bucketlist_name = 'Make the world a better place'
        self.bucketlist = Bucketlists(name=self.bucketlist_name)

    def test_can_create_a_bucketlist(self):
        """Test the creation of a new bucketlist."""
        current_count = Bucketlists.objects.count()
        self.bucketlist.save()
        new_count = Bucketlists.objects.count()
        self.assertNotEqual(current_count, new_count)

class UserModelTestCase(TestCase):
    """Tests for the Users model"""
    def setUp(self):
        """Setup the users model"""
        self.user_name = 'OptimusPrime'
        self.new_user = User(name=self.user_name)

    def test_creation_of_new_user(self):
        """Test it can create a new user"""
        current_count = User.Objects.count()
        self.new_user.save()
        new_count = User.Objects.count()
        self.assertNotEqual(current_count, new_count)


