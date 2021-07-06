# Generated by Django 3.2.4 on 2021-07-06 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('farms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Investment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('investment_amount', models.IntegerField()),
                ('duration', models.DurationField(help_text='in years')),
                ('end_date', models.DateTimeField(blank=True, help_text='End date of investment', null=True)),
                ('start_date', models.DateTimeField(blank=True, help_text='Start date of investment', null=True)),
                ('farm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farms.farm')),
            ],
        ),
    ]
