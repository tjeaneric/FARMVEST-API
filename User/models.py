from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django_countries.fields import CountryField
# Create your models here.


class User(AbstractUser):
    
    def Gender():
        """
        Choices of Gender.
        """
        Gender= {
        'MALE': 'MALE',
        'FEMALE': 'FEMALE',
        'RATHER NOT SAY':'RATHER NOT SAY'
         }
        multi_choice= []

        for choice in Gender:
            multi_choice.append((choice,Gender[choice]))
    
        return tuple(multi_choice)


    def States():

        states = {
            'Abia':'ABIA',
            'ABUJA':'ABUJA',
            'ADAMAWA': 'ADAMAWA',
            'AKWA IBOM':'AKWA IBOM',
            'ANAMBRA':'ANAMBRA',
            'BAUCHI':'BAUCHI',
            'BAYELSA':'BAYELSA',
            'BENUE':'BENUE',
            'BORNO':'BORNO',
            'CROSS RIVER':'CROSS RIVER',
            'DELTA':'DELTA',
            'EBONYI':'EBONYI',
            'EDO':'EDO',
            'EKITI':'EKITI',
            'ENUGU':'ENUGU',
            'GOMBE':'GOMBE',
            'IMO':'IMO',
            'JIGAWA':'JIGAWA',
            'KADUNA':'KADUNA',
            'KANO':'KANO',
            'KATSINA':'KATSINA',
            'KEBBI':'KEBBI',
            'KOGI':'KOGI',
            'KWARA':'KWARA',
            'LAGOS':'LAGOS',
            'NASAWARA':'NASAWARA',
            'NIGER':'NIGER',
            'OGUN':'OGUN',
            'ONDO':'ONDO',
            'OSUN':'OSUN',
            'OYO':'OYO',
            'PLATEAU':'PLATEAU',
            'RIVERS':'RIVERS',
            'SOKOTO':'SOKOTO',
            'TARABA':'TARABA',
            'YOBE':'YOBE',
            'ZAMFARA':'ZAMFARA',
        }
        multi_choice= []

        for choice in states:
            multi_choice.append((choice,states[choice]))
    
        return tuple(multi_choice)

    phoneNumberRegex = RegexValidator(regex=r"^\+?234?\d(8,15)$")
    phone_number=models.CharField(validators=[phoneNumberRegex],max_length=16,unique= True)
    gender = models.CharField(max_length=19, choices=Gender(),default='RATHER NOT SAY')
    date_of_birth = models.DateField(null=True,blank=True)
    updated_at = models.DateTimeField(auto_now_add= True)
    bank_name = models.CharField(max_length= 25)
    account_number = models.CharField(max_length=11,null= True)
    country = CountryField()
    state = models.CharField(max_length=19,default='ABUJA', choices=States(),null=True)
    address = models.TextField()


    def __str__(self):
        return self.username        

