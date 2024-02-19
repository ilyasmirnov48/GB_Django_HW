from django.core.management.base import BaseCommand
from myapp.models import Order, Client, Product
import random


class Command(BaseCommand):
    help = "Generate fake order."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Order ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        clients = Client.objects.all()
        products = Product.objects.all()
        for i in range(1, count + 1):
            products_list = random.sample(list(products), 5)
            for product in products_list:
                total_price = 1
                total_price += product.price * products_list.count(product)
            orders = Order.objects.create(
                customer=random.choice(clients),
                total_price=total_price
            )
            orders.products.set(products_list)
            orders.save()
