# Generated by Django 4.0.4 on 2022-04-29 08:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('E_app', '0005_rename_product_cart_product_remove_cart_ordered'),
    ]

    operations = [
        migrations.RenameField(
            model_name='Cart',
            old_name='product',
            new_name='Product',
        ),
    ]
