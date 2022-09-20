from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_address = models.CharField(max_length=100)
    mobileno = models.CharField(max_length=10)


class Customer(models.Model):
    address = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_number = models.CharField(max_length=100)