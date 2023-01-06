from django.db import models

class Users(models.Model):

    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=15)
    birth = models.DateField()

