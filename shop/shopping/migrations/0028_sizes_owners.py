# Generated by Django 3.0 on 2019-12-26 12:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0027_additem_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='sizes',
            name='owners',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shopping.Profile'),
        ),
    ]
