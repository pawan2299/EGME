# Generated by Django 3.0 on 2020-01-05 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0047_additem_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='ordered',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopping.Profile')),
                ('it', models.ManyToManyField(to='shopping.OrderItem')),
            ],
        ),
    ]