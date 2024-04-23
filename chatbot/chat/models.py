from django.db import models

# Create your models here.
class Contact(models.Model):
    userName=models.CharField(max_length=50)
    phoneNumber=models.CharField(max_length=15)
    