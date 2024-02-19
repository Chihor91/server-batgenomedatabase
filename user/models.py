from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
import os

# Create your models here.
class AccountManager(BaseUserManager):
    def create_superuser(self, email, username, password, **other_fields):
        other_fields.setdefault('is_superuser', True)

        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be superuser=True.'
            )
        
        return self.create_user(email, username, password, **other_fields)
    
    def create_user(self, email, username, password, **other_fields):
        if not email:
            raise ValueError(('You must provide an email address'))
        
        email = self.normalize_email(email)
        user = self.model(email=email, username=username,
                          **other_fields)
        user.set_password(password)
        user.save()
        return user
    
class Account(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(('email address'), unique=True)
    username = models.CharField(max_length=150, unique=True)
    date_created = models.DateTimeField(default=timezone.now)

    objects = AccountManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username
