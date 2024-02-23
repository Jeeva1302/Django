from django.db import models

# Create your models here.

class Employee(models.Model):
    
    Firstname = models.CharField(max_length=200)
    Lastname = models.CharField(max_length=200)
    Qualification = models.CharField(max_length=100)
    Experience = models.IntegerField()
    Email = models.EmailField(max_length=254)
    Phonenumber = models.BigIntegerField()
    streetadress = models.CharField(max_length=200)
    State = models.CharField(max_length=100)
    Country = models.CharField(max_length=100)
    Zipcode = models.CharField(max_length=200)
    Areacode = models.CharField(max_length=50)