from rest_framework import serializers

from amappy.users.models import User


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [
            "id", "username", "email", "first_name", "last_name",
            "phone_number", "is_distributor", "is_supervisor", "url",
        ]
