import farms
from django.db import models
from farms.models import Farm
from django.db.models import DateTimeField
import User
from User.models import User
from django.conf import settings
# Create your models here.

class Investment(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    #from_id= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #to_id= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    investment_amount = models.IntegerField()
    duration = models.DurationField(help_text="in years")
    end_date = models.DateTimeField(null=True,blank=True,help_text='End date of investment')
    start_date = models.DateTimeField(null=True,blank=True,help_text='Start date of investment')

   
   
