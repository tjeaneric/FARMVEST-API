from django.db import models
from django.db.models.fields.related import ForeignKey
from User.models import User
from django.conf import settings
from User.constants import Role


# from .dictionary import Payment_Method

# Create your models here.
class Wallet(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    wallet_amount = models.BigIntegerField()

    def __str__(self):
        return self.name