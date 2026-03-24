from rest_framework.viewsets import ModelViewSet

from core.models import Veiculo
from core.serializers.veiculo import VeiculoListSerializer, VeiculoSerializer


class VeiculoViewSet(ModelViewSet):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer

    def get_serializer_class(self):
        if self.action == {'list', 'retrieve'}:
            return VeiculoListSerializer
        return VeiculoSerializer
