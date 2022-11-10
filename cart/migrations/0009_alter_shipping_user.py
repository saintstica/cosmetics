# Generated by Django 4.1.1 on 2022-11-07 12:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cart', '0008_rename_address_shipping_delivery_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipping',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]