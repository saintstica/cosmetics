# Generated by Django 4.1.1 on 2022-11-01 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='created',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]