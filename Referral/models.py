import User
from django.db import models
from User.models import User
from django.conf import settings


class Referral(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    referral_bonus = models.IntegerField()
