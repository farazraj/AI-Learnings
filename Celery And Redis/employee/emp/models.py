from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# class CustomUser(AbstractUser):
#     reg_code = models.IntegerField()


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add additional fields here
    reg_code = models.IntegerField()
   
# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length = 100, null = True)
    phone = models.CharField(max_length = 100, null = True)


    def __str__(self):
        return str(self.name) or ''


