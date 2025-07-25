from django.db.models.signals import post_save
from django.dispatch import receiver
from parking.models import ParkingRecord


@receiver(post_save, sender=ParkingRecord)
def update_parking_spot_status(sender, instance, created, **kwargs):
    """
    Atualiza automaticamente o status de uma vaga de estacionamento
    (ParkingSpot) sempre que um registro de estacionamento
    (ParkingRecord) é salvo.

    Esta função é um "receiver" do sinal `post_save` do Django, conectado
    especificamente ao modelo `ParkingRecord`. Ela é acionada toda vez que
    um `ParkingRecord` é criado ou atualizado.

    A lógica de atualização é baseada no campo `exit_time` do registro:
    - Se `exit_time` for nulo, a vaga é marcada como ocupada
        (`is_occupied = True`).
    - Se `exit_time` tiver um valor, a vaga é marcada como livre
        (`is_occupied = False`).
    """

    parking_spot = instance.parking_spot
    parking_spot.is_occupied = instance.exit_time is None
    parking_spot.save()
