from rest_framework import serializers

class BandaSerializer(serializers.Serializer):
    nome = serializers.CharField(max_length=100)