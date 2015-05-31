from rest_framework import viewsets

from amappy.users.models import AmapUser
from amappy.users.serializers import AmapUserSerializer


# ViewSets define the view behavior.
class AmapUserViewSet(viewsets.ModelViewSet):
    queryset = AmapUser.objects.all()
    serializer_class = AmapUserSerializer
