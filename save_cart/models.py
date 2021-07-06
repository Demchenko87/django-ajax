from django.db import models

class Save_cart(models.Model):
    # id_product = models.CharField('ID продукта', max_length=1000, blank=True, null=True)
    # quantity = models.CharField('Количество продукта', blank=True, null=True, max_length=1000)
    session_cart = models.TextField('Корзина заказов', blank=True, null=True, max_length=9000)
    token = models.CharField('token USER', max_length=1000, blank=True, null=True)

    def str(self):
        return self.token
