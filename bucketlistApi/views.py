from django.shortcuts import render
from rest_framework import generics
from .serializers import BucketlistsSerializer, UserSerializer
from .models import Bucketlists


class CreateView(generics.ListCreateAPIView):
    """Class for creating the bucketlists in the api."""
    queryset = Bucketlists.objects.all()
    serializer_class = BucketlistsSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()
