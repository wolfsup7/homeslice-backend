from rest_framework import serializers
from .models import Customer
from .models import Ingredients
from .models import Pizza
from .models import Order

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        field = ('id', 'name',)

class IngredientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredients
        field = ('id', 'name', 'category',)

class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        field = ('id', 'name', 'ingredients', 'price', 'image', 'creator',)

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        field = ('id', 'customer', 'pizza', 'date_created',)
        