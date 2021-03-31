from rest_framework import serializers
from .models import *


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'account_name', 'users', 'created']
