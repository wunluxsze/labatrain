from django.db import models


class Products(models.Model):
    productname = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    price = models.IntegerField()


class Cart(models.Model):
    productlist = models.ManyToManyField(Products)

class Order(models.Model):
    products = models.ManyToManyField(Cart)
    price_summ = models.IntegerField()


    def calc(self):
        sum = 0
        for product in self.products.all():
            sum += product.price

        self.price_summ = sum
        self.save()