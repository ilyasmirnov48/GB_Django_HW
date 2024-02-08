from django.core.management.base import BaseCommand
from myapp.models import Client


class Command(BaseCommand):
    help = "Generate fake client."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Client ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            client = Client(
                name=f'Name{i}',
                email=f'mail{i}@mail.ru',
                phone_number=f'8987654321{i}',
                address=f'city{i}'
            )
            client.save()
