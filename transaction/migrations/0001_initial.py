# Generated by Django 3.2.4 on 2021-07-10 08:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import utils.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [migrations.swappable_dependency(settings.AUTH_USER_MODEL)]

    operations = [
        migrations.CreateModel(
            name="Transaction",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "reference_code",
                    models.CharField(
                        default=utils.utils.generate_code, max_length=16, unique=True
                    ),
                ),
                ("amount", models.BigIntegerField()),
                (
                    "payment_method",
                    models.CharField(
                        choices=[
                            ("CREDIT CARD", "CREDIT CARD"),
                            ("PAYPAL", "PAYPAL"),
                            ("BANK TRANSFER", "BANK TRANSFER"),
                        ],
                        default="CREDIT CARD",
                        help_text="Choose your payment method",
                        max_length=20,
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("SUCCESSFUL", "SUCCESSFUL"),
                            ("UNPROCESSED", "UNPROCESSED"),
                            ("FAILED", "FAILED"),
                            ("WAITING", "WAITING"),
                        ],
                        default="UNPROCESSED",
                        max_length=50,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "receiver",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="receiver",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "sender",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sender",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        )
    ]