from django.shortcuts import render

# Create your views here.
from models import Customer, Manufacturer
from serializers import CustomerSerializer, ManufacturerSerializer
from rest_framework import viewsets


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class ManufacturerSerializerViewSet(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
