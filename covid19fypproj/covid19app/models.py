from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    is_medical = models.BooleanField('Is_medical', default=False)
    is_expert = models.BooleanField('Is_expert', default=False)

    @property
    def is_Medical(self):
        return self.is_medical
    

    @property
    def is_Expert(self):
        return self.is_expert


class MedicalExpert(models.Model):
    age = models.IntegerField
    gender = models.CharField(max_length=30)
    country = models.TextField(max_length=30)
    prediction = models.TextField(max_length=30)
    image = models.


class ITExpert(models.Model):
    age = models.IntegerField
    gender = models.CharField(max_length=30)
    country = models.TextField(max_length=30)
    prediction = models.TextField(max_length=30)

    
    






