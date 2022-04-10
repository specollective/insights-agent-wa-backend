from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, firstName, lastName, phoneNumber, email, password=None, **kwargs):
        """Create and return a `User` with a first name, last name, phone number, email, and password."""
        if firstName is None:
            raise TypeError('Users must have a first name.')
        if lastName is None:
            raise TypeError('Users must have a last name.')
        if email is None:
            raise TypError('Users must have an email.')
        if phoneNumber is None:
            raise TypError('Users must have a phone number.')
            
        user = self.model(firstName=firstName, lastName=lastName, phoneNumber=phoneNumber, email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        
        return user
        
    def create_superuser(self, username, email, password):
        """Create and return a `User` with superuser (admin) permissions"""
        if password is None:
            raise TypError('Superusers must have a password.')
        if email is None:
            raise TypError('Superusers must have an email.')
        if username is None:
            raise TypeError('Superusers must have a username.')
        
        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        
        return user
        
class User(AbstractBaseUser, PermissionsMixin):
    firstName = models.CharField(db_index=True, max_length=255)
    lastName = models.CharField(db_index=True, max_length=255)
    phoneNumber = models.CharField(db_index=True, max_length=255)
    username = models.CharField(db_index=True, max_length=255, unique=True)
    email = models.EmailField(db_index=True, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstName', 'lastName', 'email', 'phoneNumber']
    
    objects = UserManager()
    
    def __str__(self):
        return f"{self.email}"