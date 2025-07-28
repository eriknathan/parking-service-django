from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, \
    DjangoModelPermissions
from customers.models import Customer
from customers.serializers import CustomerSerializer


class CustomersViewSet(viewsets.ModelViewSet):
    '''
    Cria a API completa para gerenciar os Clientes (Customer).

    O acesso a este endpoint é restrito e permitido apenas para
    usuários administradores (com 'is_staff=True').
    '''
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [DjangoModelPermissions, IsAdminUser]
