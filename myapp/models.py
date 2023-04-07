from django.db import models

# Create your models here.

from django.db import models


class User(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    age = models.DecimalField(max_digits=10, decimal_places=2)
