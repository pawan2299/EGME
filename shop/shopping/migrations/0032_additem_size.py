# Generated by Django 3.0 on 2019-12-26 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0031_remove_additem_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='additem',
            name='size',
            field=models.CharField(choices=[('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL'), ('', '')], default='', max_length=20),
        ),
    ]
