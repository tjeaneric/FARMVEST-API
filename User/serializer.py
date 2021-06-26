from rest_framework import serializers 
from .models import User
from django_countries.serializers import CountryFieldMixin



class UserSerializer(CountryFieldMixin,serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name', 
            'username',
            'email',
            'gender',
            'date_of_birth',
            'role',
            'bank_name',
            'account_number',
            'country',
            'state',
            'address'
        ]
