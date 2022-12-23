from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=50, null=True)

class Ingredients(models.Model):
    name = models.CharField(max_length=50, null=True)
    category = models.CharField(max_length=50, null=True)

    def _str_(self):
        return self.name

class Pizza(models.Model):
    name = models.CharField(max_length=50, null=True)
    price = models.FloatField(null=True)
    image = models.URLField(max_length=200, null=True)
    creator = models.CharField(max_length=500, null=True)
    ingredients = models.ManyToManyField(Ingredients)

    def _str_(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)
    pizza = models.ForeignKey(Pizza, null=True, on_delete= models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)