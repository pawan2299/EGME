# Generated by Django 3.0 on 2019-12-27 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0034_delivery'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivery',
            name='tot',
            field=models.ManyToManyField(to='shopping.OrderItem'),
        ),
    ]