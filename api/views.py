from django.shortcuts import render
from rest_framework import viewsets

from shoestore.models import Shoe, ShoeColor, ShoeType, Manufacturer
from api.serializers import ShoeColorSerializer, ShoeSerializer, ShoeTypeSerializer, ManufacturerSerializer

# Create your views here.

class ShoeViewSet(viewsets.ModelViewSet):
    queryset = Shoe.objects.all()
    serializer_class = ShoeSerializer

class ShoeColorViewSet(viewsets.ModelViewSet):
    queryset = ShoeColor.objects.all()
    serializer_class = ShoeColorSerializer

class ShoeTypeViewSet(viewsets.ModelViewSet):
    queryset = ShoeType.objects.all()
    serializer_class = ShoeTypeSerializer

class ManufacturerViewset(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer