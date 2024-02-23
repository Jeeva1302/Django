
# Create your models here.

from django.db import models

class emp(models.Model):
    fullname = models.CharField(max_length=100)