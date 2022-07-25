from rest_framework import serializers
from .models import NpcDetails

class NpcDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NpcDetails
        fields = [
            'first_name',
            'last_name',
            'title',
            'age',
            'race',
            'gender',
            'is_alive',
            'description',
            'personality',
            'notes',
            'creation_datetime',
            'last_modified_datetime',
        ]
        read_only_fields = [
            'creation_datetime',
            'last_modified_datetime',
        ]
