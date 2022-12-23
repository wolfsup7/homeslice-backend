from django.contrib import admin

# Register your models here.
from .models import Customer
admin.site.register(Customer)
from .models import Ingredients
admin.site.register(Ingredients)
from .models import Pizza
admin.site.register(Pizza)
from .models import Order
admin.site.register(Order)
