# Generated by Django 3.2.15 on 2022-11-02 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0054_alter_cart_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
