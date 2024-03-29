# Generated by Django 3.2.4 on 2021-07-10 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("transaction", "0004_alter_transaction_status")]

    operations = [
        migrations.AlterField(
            model_name="transaction",
            name="status",
            field=models.CharField(
                choices=[
                    ("SUCCESSFUL", "SUCCESSFUL"),
                    ("UNPROCESSED", "UNPROCESSED"),
                    ("FAILED", "FAILED"),
                    ("WAITING", "WAITING"),
                ],
                default="UNPROCESSED",
                max_length=50,
            ),
        )
    ]
