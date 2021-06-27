from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django_countries.fields import CountryField
from .constants import Role,Gender,States
# Create your models here.


class User(AbstractUser):

    # phoneNumberRegex = RegexValidator(regex=r"^\+?234?\d(8,15)$")
    phone_number=models.CharField(max_length=16,unique= True,help_text='Phone Number of the user')
    gender = models.CharField(max_length=19, choices=Gender(),default='RATHER NOT SAY', help_text='Gender of the User')
    date_of_birth = models.DateField(null=True,blank=False,help_text='Date of birth of the user')
    updated_at = models.DateTimeField(auto_now_add= True, help_text='Autogenerated by the post request')
    bank_name = models.CharField(max_length= 25,help_text='The banks in Nigeria')
    role = models.CharField(max_length=9, choices=Role(),default='INVESTOR',help_text='The options are Farmer and investor')
    account_number = models.CharField(max_length=11,null= True,help_text='Account number field.' )
    country = CountryField()
    state = models.CharField(max_length=19, choices=States(),default='ABUJA',null=True,help_text='All the states in Nigeria and the FCT')
    address = models.TextField(help_text='Address of the farm')


    def __str__(self):
        return self.username        

