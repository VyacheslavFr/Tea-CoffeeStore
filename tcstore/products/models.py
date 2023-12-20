from django.db import models


class Products(models.Model):
    product_name = models.CharField('Наименование', max_length=250)
    product_vendor_code = models.CharField('Артикул', max_length=20)
    product_category = models.CharField('Категория', max_length=40)
    product_sub_category = models.CharField('Подкатегория', max_length=40)
    product_package = models.CharField('Упаковка', max_length=100)
    product_net_weight = models.CharField('Вес нетто, г.', max_length=20)
    product_full_category = models.CharField('Развёрнутая категория', max_length=40)
    product_description = models.TextField('Описание')
    product_price = models.DecimalField('Цена, руб.', max_digits=10, decimal_places=2, default=True, null=True, blank=True)
    product_available = models.BooleanField('Наличие', default=True)

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
