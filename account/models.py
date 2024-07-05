from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Acccount(models.Model):
    name = models.CharField(max_length=50)
    account_number = models.CharField(max_length=50)
    
    
class Address(models.Model):
    name = models.CharField(max_length=120, blank=True)
    address = models.CharField(max_length=120, blank=True)
    postalcode = models.CharField(max_length=20, blank=True)
    city = models.CharField(max_length=120, blank=True)
    country = models.CharField(max_length=80, blank=True)
    email = models.EmailField(blank=True)