from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models


help_text = "Number's format: '+999999999'. Up to 15 digits allowed."
phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message=help_text)


class User(AbstractUser):
    is_distributor = models.BooleanField("distributor", default=False)
    is_supervisor = models.BooleanField("supervisor", default=False)
    phone_number = models.CharField(validators=[phone_regex],
                                    max_length=15,
                                    help_text=help_text,
                                    blank=True,)

    def __unicode__(self):
        return self.username
