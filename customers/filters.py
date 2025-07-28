from dj_rql.filter_cls import AutoRQLFilterClass
from customers.models import Customer


class CustomerFilterClass(AutoRQLFilterClass):
    """
    Habilita filtros dinâmicos e avançados para o modelo 'Customer' usando RQL.

    Ao associar esta classe a uma ViewSet, a API passa a aceitar consultas
    complexas diretamente na URL, seguindo a sintaxe da RQL (Resource Query
    Language).

    Por exemplo, o cliente da API poderá fazer requisições como:
    - `?name=like="*Silva*"` (para buscar nomes que contenham "Silva")
    - `?age=gt=30` (para buscar clientes com idade maior que 30)
    - `?limit(10)&ordering(-created_at)` (para paginar e ordenar)

    A classe `AutoRQLFilterClass` faz isso de forma automática, inspecionando
    o modelo `Customer` e tornando seus campos filtráveis por padrão.
    """
    MODEL = Customer
