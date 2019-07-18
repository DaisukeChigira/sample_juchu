from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)


class Product(models.Model):
    # name = models.ForeignKey(Question, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)

    