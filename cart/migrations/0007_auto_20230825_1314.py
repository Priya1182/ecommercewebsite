# Generated by Django 3.2 on 2023-08-25 07:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0006_orderitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='cart_item',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='order',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='OrderItem',
        ),
    ]
