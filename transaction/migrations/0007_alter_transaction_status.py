# Generated by Django 3.2.4 on 2021-07-10 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("transaction", "0006_alter_transaction_status")]

    operations = [
        migrations.AlterField(
            model_name="transaction",
            name="status",
            field=models.CharField(
                choices=[
                    ("SUCCESSFUL", "SUCCESSFUL"),
                    ("WAITING", "WAITING"),
                    ("UNPROCESSED", "UNPROCESSED"),
                    ("FAILED", "FAILED"),
                ],
                default="UNPROCESSED",
                max_length=50,
            ),
        )
    ]
