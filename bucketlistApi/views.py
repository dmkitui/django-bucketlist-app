from django.shortcuts import render
from rest_framework import generics
from .serializers import BucketlistsSerializer
from .models import Bucketlists


class CreateView(generics.ListCreateAPIView):
    """Class for creating the bucketlists in the api."""
    queryset = Bucketlists.objects.all()
    serializer_class = BucketlistsSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()


class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """Class for http GET, PUT and DELETE requests."""

    queryset = Bucketlists.objects.all()
    serializer_class = BucketlistsSerializer
