from rest_framework import generics

from .models import NpcDetails
from .serializers import NpcDetailsSerializer

class NpcDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a NPC instance.
    """
    queryset = NpcDetails.objects.all()
    serializer_class = NpcDetailsSerializer

