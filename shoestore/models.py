from django.db import models

# Create your models here.

class Manufacturer(models.Model):
    name = models.CharField(max_length=50)
    website = models.CharField(max_length=150)


class ShoeType(models.Model):
    style = models.CharField(max_length=50)


class ShoeColor(models.Model):
    RED = 'Red'
    ORANGE = 'Orange'
    YELLOW = 'Yellow'
    GREEN = 'Green'
    BLUE = 'Blue'
    INDIGO = 'Indigo'
    VIOLET = 'Violet'
    BLACK = 'Black'
    WHITE = 'White'
    CHOICES = [
        (RED, 'Red'),
        (ORANGE, 'Orange'),
        (YELLOW, 'Yellow'),
        (GREEN, 'Green'),
        (BLUE, 'Blue'),
        (INDIGO, 'Indigo'),
        (VIOLET, 'Violet'),
        (BLACK, 'Black'),
        (WHITE, 'White')
    ]
    color_name = models.CharField(max_length = 8, choices=CHOICES, default=WHITE)


class Shoe(models.Model):
    size = models.IntegerField()
    brand_name = models.CharField(max_length=50)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    color = models.ForeignKey(ShoeColor, on_delete=models.CASCADE)
    material = models.CharField(max_length=50)
    shoe_type = models.ForeignKey(ShoeType, on_delete=models.CASCADE)
    fasten_type = models.CharField(max_length=50)
