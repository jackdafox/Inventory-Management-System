from django.db import models

CATEGORY = (
    ('Food', 'Food'),
    ('Electronics', 'Electronics'),
    ('Health Care', 'Health Care'),
    ('Pet Care', 'Pet Care'),
    ('Household & Cleaning Supplies', 'Household & Cleaning Supplies'),
    ('Tools', 'Tools'),
)

class Inventory(models.Model):
    inventory_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=True)

class Product(models.Model):
    inventory = models.ForeignKey(Inventory, related_name='products', on_delete=models.CASCADE, null=True, blank=True)
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=30, choices=CATEGORY, null=True)
    quantity = models.PositiveIntegerField(null=True)
    price = models.PositiveIntegerField(null=True)
        