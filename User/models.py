from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django_countries.fields import CountryField
from .constants import Role,Gender,States
# Create your models here.


class User(AbstractUser):

    phoneNumberRegex = RegexValidator(regex=r"^\+?234?\d(8,15)$")
    phone_number=models.CharField(validators=[phoneNumberRegex],max_length=16,unique= True)
    gender = models.CharField(max_length=19, choices=Gender(),default='RATHER NOT SAY')
    date_of_birth = models.DateField(null=True,blank=True)
    updated_at = models.DateTimeField(auto_now_add= True)
    bank_name = models.CharField(max_length= 25)
    role = models.CharField(max_length=9, choices=Role(),default='INVESTOR')
    account_number = models.CharField(max_length=11,null= True)
    country = CountryField()
    state = models.CharField(max_length=19, choices=States(),default='ABUJA',null=True)
    address = models.TextField()


    def __str__(self):
        return self.username        

