from django.contrib.auth.models import AbstractUser


class AmapUser(AbstractUser):

    def __unicode__(self):
        return self.username


class Distributor(AmapUser):
    pass
