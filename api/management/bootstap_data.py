from django.core.management.base import BaseCommand, CommandError
from shoestore.models import ShoeType, ShoeColor

class Command(BaseCommand):
    def handle(self, *args, **options):
        shoe_types = ['sneaker', 'boot', 'sandal', 'dress', 'other']
        shoe_colors = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet', 'White', 'Black']
        for shoe in shoe_types:
            ShoeType.objects.create(style=shoe)
        for shoe in shoe_colors:
            ShoeColor.objects.create(color_name=shoe)
        