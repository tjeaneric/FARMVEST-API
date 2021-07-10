from django.db import models
from django.conf import settings


class Wallet(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    wallet_amount = models.BigIntegerField()

    def __str__(self):
        return self.name
