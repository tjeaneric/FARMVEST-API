from django.db import models
from User.models import User
from django.conf import settings
from utils.utils import generate_code
from User.constants import Role
from .dictionary import Payment_Method


# Create your models here.


class Transaction(models.Model):
    reference_code = models.CharField(max_length=16, default=generate_code, unique=True)
    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="sender"
    )
    receiver = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="receiver"
    )
    amount = models.BigIntegerField()
    payment_method = models.CharField(
        max_length=20,
        choices=Payment_Method(),
        default="CREDIT CARD",
        help_text="Choose your payment method",
    )
    statuses = {
        ("UNPROCESSED", "UNPROCESSED"),
        ("WAITING", "WAITING"),
        ("SUCCESSFUL", "SUCCESSFUL"),
        ("FAILED", "FAILED"),
    }

    status = models.CharField(max_length=50, choices=statuses, default="UNPROCESSED")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.reference_code
