from django.db import models

class Product(models.Model):
    name = models.CharField('Название продукта', max_length=1000, blank=True, null=True)
    description = models.TextField('Описание продукта', blank=True, null=True, max_length=1000)
    price = models.CharField('стоимость продукта', max_length=30, blank=True, null=True)
    image = models.ImageField('Изображение', blank=True, null=True)

    def str(self):
        return self.name
