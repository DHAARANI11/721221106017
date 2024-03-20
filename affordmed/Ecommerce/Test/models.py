from django.db import models
from django.contrib.auth.models import AbstractUser

class User(models.Model):

    companyName=models.CharField(max_length=20,null=True)

    ownerName=models.CharField(max_length=20,null=True)

    rollNo=models.IntegerField(null=True)

    ownerEmail=models.EmailField(max_length=30)

    accessCode=models.CharField(max_length=10)


    def __str__(self):
        return self.rollNo


class Companies(models.Model):

    COMPANIES={
        ("AMZ"),
        ("FLP"),
        ("SNP"),
        ("MYN"),
        ("AZO")
    }


class Product(models.Model):

    

    productName=models.CharField(max_length=20,null=True)
    price=models.IntegerField(null=True)
    ratings=models.DecimalField(max_digits=10,decimal_places=4, blank=True, null=True)
    discount=models.IntegerField()
    availability=models.CharField(max_length=20)
