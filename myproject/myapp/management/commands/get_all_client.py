from django.core.management.base import BaseCommand
from myapp.models import Client


class Command(BaseCommand):
    help = "Get all client."

    def handle(self, *args, **kwargs):
        clients = Client.objects.all()
        self.stdout.write(f'{clients}')
