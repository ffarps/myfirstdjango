from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField('Name',max_length=255)
    price = models.FloatField('Price')
    stock = models.IntegerField("Stock")
    def __str__(self):
        return self.name
class Client(models.Model):
    name=models.CharField('Name',max_length=255)
    email=models.CharField('Email',max_length=255)
    def __str__(self):
        return self.name