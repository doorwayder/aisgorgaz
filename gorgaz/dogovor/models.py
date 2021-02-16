from django.db import models
from django.contrib.auth.models import User


class Dogovor(models.Model):
    name = models.CharField(max_length=200, verbose_name='ФИО')
    number = models.CharField(max_length=10, verbose_name='Номер договора')
    date = models.DateField(auto_now_add=True, verbose_name='Даза заключения договора')
    end_date = models.DateField(blank=False, verbose_name='Даза окончания договора')
    tel1 = models.CharField(max_length=12, blank=True, verbose_name='Телефон 1')
    tel2 = models.CharField(max_length=12, blank=True, verbose_name='Телефон 2')
    tel3 = models.CharField(max_length=12, blank=True, verbose_name='Телефон 3')
    fiz = models.BooleanField(verbose_name='Физлицо')
    address_city = models.CharField(max_length=100, verbose_name='Населенный пункт')
    address_street = models.CharField(max_length=200, verbose_name='Улица')
    address_house = models.CharField(max_length=20, verbose_name='Дом')
    address_kv = models.IntegerField(verbose_name='Квартира')
    equip = models.CharField(max_length=100, verbose_name='Оборудование')
    sum = models.IntegerField(verbose_name='Сумма')
    discount = models.IntegerField(verbose_name='Скидка')
    amount = models.IntegerField(verbose_name='Итого')
    comment = models.CharField(max_length=500, blank=True, verbose_name='Примечание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Договор'
        verbose_name_plural = 'Договора'

