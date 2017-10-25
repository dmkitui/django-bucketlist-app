from django.db import models


class Bucketlists(models.Model):
    """The bucketlist model."""
    name = models.CharField(max_length=255, blank=False, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)

class User(models.Model):
    """The User model"""
    user_name = models.CharField(max_length=255, blank=False, unique=True)
    date_registered = models.DateTimeField(auto_now_add=True)