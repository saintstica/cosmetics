# Generated by Django 4.1.1 on 2022-11-01 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0007_alter_shipping_billing_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shipping',
            old_name='address',
            new_name='delivery_address',
        ),
        migrations.RemoveField(
            model_name='shipping',
            name='order_address',
        ),
        migrations.AlterField(
            model_name='shipping',
            name='billing_address',
            field=models.CharField(max_length=250),
        ),
    ]
