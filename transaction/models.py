from django.db import models
from User.models import User
from django.conf import settings
from User.constants import Role
from .dictionary import Payment_Method
# Create your models here.

class Transaction(models.Model):
    investor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100, default= "User's name")
    #from_id= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #to_id= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    amount= models.IntegerField()
    transaction_name= models.TextField()
    transaction_date= models.DateTimeField(auto_now_add= True, help_text='Autogenerated by the post request')
    payment_method=models.CharField(max_length=20, choices=Payment_Method(),default='CREDIT CARD', help_text='Choose your payment method')
    
    def __str__(self):
        return self.user_name