from django.contrib.auth.models import AbstractUser
from django.db import models


class AmapUser(AbstractUser):
    def __unicode__(self):
        return self.username


class Distributor(AmapUser):
    is_distributor = models.BooleanField("distributor", default=False)


class Supervisor(Distributor):
    is_supervisor = models.BooleanField("supervisor", default=False)
