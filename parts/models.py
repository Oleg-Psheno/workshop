from django.db import models

class Brand(models.Model):
    class Meta:
        verbose_name = 'производитель'
        verbose_name_plural = 'производители'
    name = models.CharField(max_length=128)
    country = models.CharField(max_length=128) # TODO add countries

    def __str__(self):
        return f'{self.name}'


class Part(models.Model):
    class Meta:
        verbose_name = 'запчасть'
        verbose_name_plural = 'запчасти'

    part_number = models.CharField(max_length=128)
    in_stock = models.BooleanField(verbose_name='наличие')
    quantity = models.IntegerField(verbose_name='количество на складе')
    name = models.CharField(max_length=128, verbose_name='наименование')
    brand = models.ForeignKey(to=Brand, on_delete=models.CASCADE) # что делать при удалении
    # category = добавить категории
    price_in = models.IntegerField(default=0)
    customer_price = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.name} {self.brand.name}'