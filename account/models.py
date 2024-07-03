from django.db import models

# Create your models here.
class Acccount(models.Model):
    name = models.CharField(max_length=50)
    account_number = models.CharField(max_length=50)
    
    