from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import CustomerSerializer
from .serializers import IngredientsSerializer
from .serializers import PizzaSerializer
from .serializers import OrderSerializer 
from .models import Customer
from .models import Ingredients
from .models import Pizza
from .models import Order

class CustomerList(generics.ListCreateAPIView):
    queryset = Customer.objects.all().order_by('id') 
    serializer_class = CustomerSerializer 

class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all().order_by('id')
    serializer_class = CustomerSerializer

class IngredientsList(generics.ListCreateAPIView):
    queryset = Ingredients.objects.all().order_by('id') 
    serializer_class = IngredientsSerializer 

class IngredientsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ingredients.objects.all().order_by('id')
    serializer_class = IngredientsSerializer

class PizzaList(generics.ListCreateAPIView):
    queryset = Pizza.objects.all().order_by('id') 
    serializer_class = PizzaSerializer 

class PizzaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pizza.objects.all().order_by('id')
    serializer_class = PizzaSerializer

class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all().order_by('id') 
    serializer_class = OrderSerializer 

class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all().order_by('id')
    serializer_class = OrderSerializer
