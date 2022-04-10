from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, firstName, lastName, phoneNumber, email, password=None, **kwargs):
        """Create and return a `User` with a first name, last name, phone number, email, and password."""
        if firstName is None:
            raise TypeError('Users must have a first name')
        if lastName is None:
            raise TypeError('Users must have a last name')
        