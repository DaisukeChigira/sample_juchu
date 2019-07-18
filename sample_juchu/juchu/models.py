from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)


class Product(models.Model):
    # name = models.ForeignKey(Question, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)

    
class Order(models.Model):
    date = models.DateField(auto_now=True)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)

    
class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.IntegerField(default=1)

