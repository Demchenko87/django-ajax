# Generated by Django 3.2.5 on 2021-07-06 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Название продукта')),
                ('description', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Описание продукта')),
                ('price', models.CharField(blank=True, max_length=30, null=True, verbose_name='стоимость продукта')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Изображение')),
            ],
        ),
    ]
