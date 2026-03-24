from rest_framework import serializers

from core.models import Veiculo


class VeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veiculo
        fields = '__all__'


class VeiculoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veiculo
        fields = '__all__'
        depth = 1
