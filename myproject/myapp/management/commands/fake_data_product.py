from django.core.management.base import BaseCommand
from myapp.models import Product
import random


class Command(BaseCommand):
    help = "Generate fake product."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Product ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            product = Product(
                name=f'Product{i}',
                description=f'Product{i} is bla bla bla many long text',
                price=(random.uniform(10.00, 999999.99)),
                quantity=(random.randint(1, 50))
            )
            product.save()
