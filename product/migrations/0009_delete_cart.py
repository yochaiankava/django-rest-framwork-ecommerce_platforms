# Generated by Django 4.2.4 on 2023-08-29 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_alter_cart_product_alter_product_category'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cart',
        ),
    ]
