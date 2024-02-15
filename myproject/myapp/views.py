from django.shortcuts import render, get_object_or_404
from .models import Client, Order
from django.http import HttpRequest
from datetime import date, timedelta


def index(request):
    return render(request, 'myapp/index.html')


def client_orders(request: HttpRequest, client_id):
    client = get_object_or_404(Client, pk=client_id)
    order_id = Order.objects.filter(customer=client).all()
    return render(request, 'myapp/client_orders.html', {'client': client, 'orders': order_id})


def order_products(request: HttpRequest, order_id):
    order = get_object_or_404(Order, pk=order_id)
    products = Order.objects.filter(id=order_id).all()
    return render(request, 'myapp/order_products.html', {'order': order, 'products': products})


def product_time(request: HttpRequest, pk):
    user = Client.objects.get(id=pk)
    today = date.today()
    week_delta = today - timedelta(days=7)
    month_delta = today - timedelta(days=30)
    year_delta = today - timedelta(days=365)
    orders_week = Order.objects.filter(customer=user, date_ordered__gte=week_delta).all()
    orders_month = Order.objects.filter(customer=user, date_ordered__gte=month_delta).all()
    orders_year = Order.objects.filter(customer=user, date_ordered__gte=year_delta).all()
    return render(request, 'myapp/product_time.html',
                  {'orders_week': orders_week, 'orders_month': orders_month, 'orders_year': orders_year})
