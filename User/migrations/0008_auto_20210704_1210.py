# Generated by Django 3.2.4 on 2021-07-04 12:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import utils.utils


class Migration(migrations.Migration):

    dependencies = [("User", "0007_user_phone_number")]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="account_number",
            field=models.CharField(
                blank=True, help_text="Account number field.", max_length=11, null=True
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="state",
            field=models.CharField(
                blank=True,
                choices=[
                    ("ABIA", "ABIA"),
                    ("ABUJA", "ABUJA"),
                    ("ADAMAWA", "ADAMAWA"),
                    ("AKWA IBOM", "AKWA IBOM"),
                    ("ANAMBRA", "ANAMBRA"),
                    ("BAUCHI", "BAUCHI"),
                    ("BAYELSA", "BAYELSA"),
                    ("BENUE", "BENUE"),
                    ("BORNO", "BORNO"),
                    ("CROSS RIVER", "CROSS RIVER"),
                    ("DELTA", "DELTA"),
                    ("EBONYI", "EBONYI"),
                    ("EDO", "EDO"),
                    ("EKITI", "EKITI"),
                    ("ENUGU", "ENUGU"),
                    ("GOMBE", "GOMBE"),
                    ("IMO", "IMO"),
                    ("JIGAWA", "JIGAWA"),
                    ("KADUNA", "KADUNA"),
                    ("KANO", "KANO"),
                    ("KATSINA", "KATSINA"),
                    ("KEBBI", "KEBBI"),
                    ("KOGI", "KOGI"),
                    ("KWARA", "KWARA"),
                    ("LAGOS", "LAGOS"),
                    ("NASAWARA", "NASAWARA"),
                    ("NIGER", "NIGER"),
                    ("OGUN", "OGUN"),
                    ("ONDO", "ONDO"),
                    ("OSUN", "OSUN"),
                    ("OYO", "OYO"),
                    ("PLATEAU", "PLATEAU"),
                    ("RIVERS", "RIVERS"),
                    ("SOKOTO", "SOKOTO"),
                    ("TARABA", "TARABA"),
                    ("YOBE", "YOBE"),
                    ("ZAMFARA", "ZAMFARA"),
                ],
                default="ABUJA",
                help_text="All the states in Nigeria and the FCT",
                max_length=19,
                null=True,
            ),
        ),
        migrations.CreateModel(
            name="Verification",
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
                    "code",
                    models.CharField(
                        default=utils.utils.generate_code, max_length=16, unique=True
                    ),
                ),
                ("is_active", models.BooleanField(default=True)),
                ("is_used", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]