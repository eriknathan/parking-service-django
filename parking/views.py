from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions
from core.permissions import IsOwnerOfVehicleOrRecord
from parking.models import ParkingRecord, ParkingSpot
from parking.serializers import ParkingRecordSerializer, ParkingSpotSerializer


class ParkingSpotViewSet(viewsets.ModelViewSet):
    '''
    Cria a API para gerenciar as Vagas de Estacionamento (ParkingSpot).

    O acesso é controlado pelo sistema de permissões padrão do Django.
    Qualquer usuário com as permissões apropriadas pode interagir
    com este endpoint.
    '''
    queryset = ParkingSpot.objects.all()
    serializer_class = ParkingSpotSerializer
    permission_classes = [DjangoModelPermissions]


class ParkingRecordViewSet(viewsets.ModelViewSet):
    '''
    Cria a API para gerenciar os Registros de Estacionamento (ParkingRecord).

    As regras de acesso são:
    - Administradores (staff) podem ver e gerenciar todos os registros.
    - Usuários comuns (clients) só podem listar e gerenciar os registros dos
    seus próprios veículos.
    '''
    queryset = ParkingRecord.objects.all()
    serializer_class = ParkingRecordSerializer
    permission_classes = [DjangoModelPermissions, IsOwnerOfVehicleOrRecord]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return ParkingRecord.objects.all()
        return ParkingRecord.objects.filter(vehicle__owner__user=user)
