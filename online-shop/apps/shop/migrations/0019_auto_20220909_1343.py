# Generated by Django 3.1 on 2022-09-09 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0018_auto_20220909_1336'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='price',
            new_name='new_price',
        ),
        migrations.AddField(
            model_name='product',
            name='old_price',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
    ]
