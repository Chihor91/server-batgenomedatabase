from rest_framework import serializers
from .models import (
    Account,
    Log
)
from datetime import datetime
import re

class AccountSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type':'password'},write_only=True)

    class Meta:
        model = Account
        fields = [
            "id",
            "email",
            "username",
            "password",
            "is_superuser"
        ]

class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = "__all__"