from django.urls import path
from . import views

urlpatterns = [
    path('api/customer', views.CustomerList.as_view(), name='customer_list'),
    path('api/customer/<int:pk>', views.CustomerDetail.as_view(), name='customer_detail'), 
    path('api/ingredients', views.IngredientsList.as_view(), name='ingredients_list'),
    path('api/ingredients/<int:pk>', views.IngredientsDetail.as_view(), name='ingredients_detail'), 
    path('api/pizza', views.PizzaList.as_view(), name='pizza_list'),
    path('api/pizza/<int:pk>', views.PizzaDetail.as_view(), name='pizza_detail'),
    path('api/order', views.OrderList.as_view(), name='order_list'),
    path('api/order/<int:pk>', views.OrderDetail.as_view(), name='order_detail'),  
]
