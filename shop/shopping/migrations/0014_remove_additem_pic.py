# Generated by Django 3.0 on 2019-12-21 19:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0013_auto_20191221_1907'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='additem',
            name='pic',
        ),
    ]