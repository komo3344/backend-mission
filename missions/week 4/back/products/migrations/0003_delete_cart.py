# Generated by Django 4.0.1 on 2022-01-16 05:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_cart'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cart',
        ),
    ]
