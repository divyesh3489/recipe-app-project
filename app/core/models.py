from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# Create your models here.

class CustomUserManager(BaseUserManager):
    
    def create_user(self,email,password=None,**extra_field):
        if not email:
            raise ValueError("Email is not provided")
        if not password:
            raise ValueError("Password is not provided")
        user = self.model(email=self.normalize_email(email),**extra_field)
        user.set_password(password)
        user.save(using=self._db)        
        return user
    def create_superuser(self,email,password=None):
        user= self.create_user(email,password)
        user.is_staff = True
        user.is_superuser =True
        user.save(using=self._db)   
        return user     

class User(AbstractBaseUser,PermissionsMixin):
    
    email = models.EmailField(max_length=255,unique=True)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    objects = CustomUserManager()
    USERNAME_FIELD = "email"
