# Generated by Django 3.2.4 on 2021-06-28 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("User", "0005_auto_20210627_1311")]

    operations = [migrations.RemoveField(model_name="user", name="phone_number")]