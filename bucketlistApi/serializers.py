from rest_framework import serializers
from .models import Bucketlists, User


class BucketlistsSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Bucketlists
        fields = ('id', 'name', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')


class UserSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the User model fields."""
        model = User
        fields = ('id', 'user_name', 'date_registered')
        read_only_fields = ('date_registered')