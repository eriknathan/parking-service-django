from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions, IsAdminUser
from core.permissions import IsOwnerOfVehicleOrRecord
from vehicles.filters import VehicleFilterClass, VehicleTypeFilterClass
from vehicles.models import Vehicle, VehicleType
from vehicles.serializers import VehicleTypeSerializer, VehicleSerializer


class VehicleTypeViewSet(viewsets.ModelViewSet):
    '''
    Cria a API completa para gerenciar os Tipos de Veículo (ex: Carro, Moto).

    Este endpoint é restrito e só pode ser acessado por usuários que
    são administradores (ou seja, com 'is_staff=True').
    '''
    queryset = VehicleType.objects.all()
    serializer_class = VehicleTypeSerializer
    rql_filter_class = VehicleTypeFilterClass
    permission_classes = [DjangoModelPermissions, IsAdminUser]


class VehicleViewSet(viewsets.ModelViewSet):
    '''
    Cria a API completa para gerenciar Veículos (criar, ver, editar, deletar).

    As regras de acesso são simples:
    - Administradores (staff) podem ver e gerenciar todos os veículos.
    - Usuários comuns só podem listar, ver, editar e deletar os
        veículos que pertencem a eles.
    '''
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    rql_filter_class = VehicleFilterClass
    permission_classes = [DjangoModelPermissions, IsOwnerOfVehicleOrRecord]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Vehicle.objects.all()
        return Vehicle.objects.filter(owner__user=user)
