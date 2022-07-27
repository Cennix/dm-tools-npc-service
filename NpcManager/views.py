from rest_framework import generics

from . import models
from . import serializers


class NpcDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a NPC instance.
    """
    queryset = models.NpcDetails.objects.all()
    serializer_class = serializers.NpcDetailsSerializer


class NpcGraphNodes(generics.ListAPIView):
    """
    Retrieve all NPC instances, for a graphs.
    """
    queryset = models.NpcDetails.objects.all()
    serializer_class = serializers.NpcDetailsGraphSerializer


class NpcGraphLinks(generics.ListAPIView):
    """
    Retrieve all NPC relationship instances, for a graphs.
    """
    queryset = models.NpcRelationshipMapper.objects.all()
    serializer_class = serializers.NpcRelationshipGraphSerializer

