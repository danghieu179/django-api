from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from contract.models import Contract
# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    contract = GenericRelation(Contract)

    class Meta:
        app_label = 'partners'
        db_table = 'customer'


class Manufacturer(models.Model):
    title = models.CharField(max_length=100)
    manager = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    contract = GenericRelation(Contract)

    class Meta:
        app_label = 'partners'
        db_table = 'manufacturer'
