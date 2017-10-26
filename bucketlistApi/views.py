from django.shortcuts import render
from rest_framework import generics
from .serializers import BucketlistsSerializer
from .models import Bucketlists
from rest_framework import permissions
from .permissions import IsOwner


class CreateView(generics.ListCreateAPIView):
    """Class for creating the bucketlists in the api."""
    queryset = Bucketlists.objects.all()
    serializer_class = BucketlistsSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save(owner=self.request.user)


class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """Class for http GET, PUT and DELETE requests."""

    queryset = Bucketlists.objects.all()
    serializer_class = BucketlistsSerializer
