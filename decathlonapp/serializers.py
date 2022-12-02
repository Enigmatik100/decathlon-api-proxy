from rest_framework import serializers


class SportSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    probability = serializers.FloatField()


class LocationSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    probability = serializers.FloatField()


class ResponseSerializer(serializers.Serializer):
    location = LocationSerializer(many=True, read_only=True)
    sport = SportSerializer(many=True, read_only=True)
