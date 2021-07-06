# Generated by Django 3.2.4 on 2021-07-05 16:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Farm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(choices=[('ABIA', 'ABIA'), ('ABUJA', 'ABUJA'), ('ADAMAWA', 'ADAMAWA'), ('AKWA IBOM', 'AKWA IBOM'), ('ANAMBRA', 'ANAMBRA'), ('BAUCHI', 'BAUCHI'), ('BAYELSA', 'BAYELSA'), ('BENUE', 'BENUE'), ('BORNO', 'BORNO'), ('CROSS RIVER', 'CROSS RIVER'), ('DELTA', 'DELTA'), ('EBONYI', 'EBONYI'), ('EDO', 'EDO'), ('EKITI', 'EKITI'), ('ENUGU', 'ENUGU'), ('GOMBE', 'GOMBE'), ('IMO', 'IMO'), ('JIGAWA', 'JIGAWA'), ('KADUNA', 'KADUNA'), ('KANO', 'KANO'), ('KATSINA', 'KATSINA'), ('KEBBI', 'KEBBI'), ('KOGI', 'KOGI'), ('KWARA', 'KWARA'), ('LAGOS', 'LAGOS'), ('NASAWARA', 'NASAWARA'), ('NIGER', 'NIGER'), ('OGUN', 'OGUN'), ('ONDO', 'ONDO'), ('OSUN', 'OSUN'), ('OYO', 'OYO'), ('PLATEAU', 'PLATEAU'), ('RIVERS', 'RIVERS'), ('SOKOTO', 'SOKOTO'), ('TARABA', 'TARABA'), ('YOBE', 'YOBE'), ('ZAMFARA', 'ZAMFARA')], default='ABUJA', help_text='All the states in Nigeria and the FCT', max_length=19, null=True)),
                ('funds_needed', models.IntegerField()),
                ('roi', models.DecimalField(decimal_places=5, help_text='in percentage', max_digits=20)),
                ('duration', models.DurationField(help_text='in years')),
                ('product', models.CharField(max_length=50)),
                ('farm_type', models.CharField(choices=[('CROPS', 'CROPS'), ('LIVESTOCK', 'LIVESTOCK')], default='CROPS', max_length=15)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='category_images')),
                ('description', models.TextField()),
                ('is_active', models.BooleanField(default=True)),
                ('farmer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
