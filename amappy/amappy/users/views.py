from rest_framework import viewsets

from amappy.users.models import (
    AmapUser,
    Distributor,
    Supervisor,
)
from amappy.users.serializers import (
    AmapUserSerializer,
    DistributorSerializer,
    SupervisorSerializer,
)


# ViewSets define the view behavior.
class AmapUserViewSet(viewsets.ModelViewSet):
    queryset = AmapUser.objects.all()
    serializer_class = AmapUserSerializer


class DistributorViewSet(viewsets.ModelViewSet):
    queryset = Distributor.objects.all().filter(is_distributor=True)
    serializer_class = DistributorSerializer


class SupervisorViewSet(viewsets.ModelViewSet):
    queryset = Supervisor.objects.all().filter(is_supervisor=True)
    serializer_class = SupervisorSerializer
