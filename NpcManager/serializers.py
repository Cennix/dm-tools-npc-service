from rest_framework import serializers
from .models import NpcDetails, NpcRelationshipMapper

class NpcRelationshipMapper(serializers.ModelSerializer):
    origin_npc = serializers.SlugRelatedField(read_only=True, slug_field="full_name")
    target_npc = serializers.SlugRelatedField(read_only=True, slug_field="full_name")

    class Meta:
        model = NpcRelationshipMapper
        fields = [
            'origin_npc',
            'target_npc',
            'overview',
            'details',
            'age',
            'ongoing',
            'weighting',
        ]

class NpcDetailsSerializer(serializers.ModelSerializer):
    origin_relationship = NpcRelationshipMapper(read_only=True, many=True)
    target_relationship = NpcRelationshipMapper(read_only=True, many=True)

    class Meta:
        model = NpcDetails
        depth = 2
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

            'origin_relationship',
            'target_relationship',
        ]
        read_only_fields = [
            'creation_datetime',
            'last_modified_datetime',
        ]
