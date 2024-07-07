from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)
    organization = models.ForeignKey('Organization', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.username

class Organization(models.Model):
    name = models.CharField(max_length=100)
    email_domain = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
