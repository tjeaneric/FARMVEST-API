from .models import Transaction
from rest_framework import serializers
#from django_countries.serializers import CountryFieldMixin

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = "__all__"
