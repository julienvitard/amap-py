from rest_framework import viewsets
from amappy.users.models import (
    User,
    Distributor,
    Supervisor,
)
from amappy.users.serializers import UserSerializer


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class DistributorViewSet(viewsets.ModelViewSet):
    queryset = Distributor.objects.all().filter(is_distributor=True)
    serializer_class = UserSerializer


class SupervisorViewSet(viewsets.ModelViewSet):
    queryset = Supervisor.objects.all().filter(is_supervisor=True)
    serializer_class = UserSerializer
