# Generated by Django 3.2.5 on 2021-07-06 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('save_cart', '0002_save_cart_token'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='save_cart',
            name='id_product',
        ),
        migrations.RemoveField(
            model_name='save_cart',
            name='quantity',
        ),
        migrations.AddField(
            model_name='save_cart',
            name='session_cart',
            field=models.TextField(blank=True, max_length=9000, null=True, verbose_name='Корзина заказов'),
        ),
    ]