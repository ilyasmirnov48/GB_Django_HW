from django.urls import path
from .views import index, client_orders, order_products, product_time


urlpatterns = [
    path('index/', index, name='index'),
    path('client/<int:client_id>/', client_orders, name='client_orders'),
    path('order/<int:order_id>/', order_products, name='order_products'),
    path('time/<int:pk>/', product_time, name='product_time'),
]
