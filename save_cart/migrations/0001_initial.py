# Generated by Django 3.2.5 on 2021-07-06 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Save_cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_product', models.CharField(blank=True, max_length=1000, null=True, verbose_name='ID продукта')),
                ('quantity', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Количество продукта')),
            ],
        ),
    ]
