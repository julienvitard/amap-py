from rest_framework import serializers

from amappy.users.models import AmapUser


# Serializers define the API representation.
class AmapUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AmapUser
        fields = ("id", "username", "email", "first_name", "last_name")
