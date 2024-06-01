from django.core.management.base import BaseCommand
from product.models import Inventory

class Command(BaseCommand):
    help = 'Creates an Inventory object'

    def handle(self, *args, **kwargs):
        # Check if an Inventory object already exists
        if not Inventory.objects.exists():
            # Create the Inventory object
            Inventory.objects.create()
            self.stdout.write(self.style.SUCCESS('Inventory created successfully'))
        else:
            self.stdout.write(self.style.WARNING('Inventory already exists'))