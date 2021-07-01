from django.db import models
from User.models import User
from django.conf import settings
from User.constants import States, farmtype


# Create your models here.


class Farm(models.Model):
    farmer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    location = models.CharField(
        max_length=19,
        choices=States(),
        default="ABUJA",
        null=True,
        help_text="All the states in Nigeria and the FCT",
    )
    funds_needed = models.IntegerField()
    roi = models.DecimalField(
        decimal_places=5, max_digits=20, help_text="in percentage"
    )
    duration = models.DurationField(help_text="in years")
    product = models.CharField(max_length=50)
    farm_type = models.CharField(
        max_length=15, choices=farmtype(), default="CROPS", null=False
    )
    thumbnail = models.ImageField(upload_to="category_images", null=True, blank=True)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
