# Generated by Django 5.0 on 2024-01-03 01:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_alter_product_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('inventory_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.product')),
            ],
        ),
    ]
