from msilib.schema import Class
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Thing(AbstractUser):
    name = models.CharField()
    description = models.CharField()
    quantity = models.IntegerField()
