from rest_framework import serializers

from amappy.users.models import (
    AmapUser,
    Distributor,
    Supervisor,
)


base_fields = [
    "id", "username", "email", "first_name", "last_name"
]


# Serializers define the API representation.
class AmapUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AmapUser
        fields = base_fields


class DistributorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Distributor
        fields = base_fields + ["is_distributor"]


class SupervisorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Supervisor
        fields = base_fields + ["is_distributor", "is_supervisor"]