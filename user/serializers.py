from rest_framework import serializers
from .models import Account
from datetime import datetime
import re

class AccountSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type':'password'},write_only=True)

    class Meta:
        model = Account
        fields = [
            "email",
            "username",
            "password"
        ]