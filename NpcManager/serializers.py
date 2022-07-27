from rest_framework import serializers
from .models import NpcDetails, NpcRelationshipMapper

class NpcRelationshipSerializer(serializers.ModelSerializer):
    origin_npc = serializers.StringRelatedField(read_only=True)
    target_npc = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = NpcRelationshipMapper
        fields = [
            'origin_npc',
            'target_npc',
            'overview',
            'details',
            'event_age',
            'ongoing',
            'weighting',
        ]


class NpcRelationshipGraphSerializer(serializers.ModelSerializer):
    source = serializers.StringRelatedField(read_only=True, source="origin_npc")
    target = serializers.StringRelatedField(read_only=True, source="target_npc")

    class Meta:
        model = NpcRelationshipMapper
        fields = [
            'source',
            'target',
            'weighting',
        ]


class NpcDetailsSerializer(serializers.ModelSerializer):
    origin_relationship = NpcRelationshipSerializer(read_only=True, many=True)
    target_relationship = NpcRelationshipSerializer(read_only=True, many=True)

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


class NpcDetailsGraphSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField(source="full_name")
    class Meta:
        model = NpcDetails
        depth = 2
        fields = [
            'pk',
            'id',
        ]
