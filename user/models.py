from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from .manager import UserManager
# Create your models here.

class User(AbstractUser):
    username=None
    name=models.CharField(max_length=30)
    email=models.EmailField(unique=True)
    phone_number=models.CharField(max_length=10)
    
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]
    
    objects=UserManager()
