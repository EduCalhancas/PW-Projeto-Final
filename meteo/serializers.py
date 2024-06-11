from rest_framework import serializers

class PrevisaoSerializer(serializers.Serializer):
    cidade = serializers.CharField(max_length=100)
    temp_min = serializers.FloatField()
    temp_max = serializers.FloatField()
    data = serializers.DateField()
    descricao_tempo = serializers.CharField(max_length=255)
    precipitacao = serializers.FloatField()
    icon_url = serializers.URLField()