# Generated by Django 3.1 on 2022-09-12 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0019_auto_20220909_1343'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='new_price',
            new_name='price',
        ),
    ]
