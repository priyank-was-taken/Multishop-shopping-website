# Generated by Django 3.2.15 on 2022-11-02 05:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0052_alter_cart_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.product'),
        ),
    ]
