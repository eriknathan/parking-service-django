from rest_framework import permissions


class IsOwnerOfVehicleOrRecord(permissions.BasePermission):
    '''
    Verifica se o user da requisição é o dono do objeto que ele tenta acessar.

    Esta permissão é flexível e funciona em dois cenários:
    1. Se o objeto em si tem um dono (ex: um Veículo).
    2. Se o objeto está ligado a um Veículo que tem um dono.

    Se nenhuma dessas condições for verdadeira, o acesso é negado.
    '''

    def has_object_permission(self, request, view, obj):
        user = request.user

        if hasattr(obj, 'owner'):
            return obj.owner and obj.owner.user == user

        if hasattr(obj, 'vehicle') and hasattr(obj.vehicle, 'owner'):
            return obj.vehicle.owner and obj.vehicle.owner.user == user

        return False
