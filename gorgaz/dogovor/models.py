from django.db import models
from django.contrib.auth.models import User


class Dogovor(models.Model):
    name = models.CharField(max_length=200, blank=True, verbose_name='ФИО')
    number = models.CharField(max_length=15, blank=True, verbose_name='Номер договора')
    date = models.DateField(blank=True, verbose_name='Даза заключения договора')
    end_date = models.DateField(blank=True, verbose_name='Даза окончания договора')
    tel1 = models.CharField(max_length=100, blank=True, verbose_name='Телефон 1')
    tel2 = models.CharField(max_length=12, blank=True, verbose_name='Телефон 2')
    tel3 = models.CharField(max_length=12, blank=True, verbose_name='Телефон 3')
    fiz = models.BooleanField(verbose_name='Физлицо')
    address_city = models.CharField(max_length=100, blank=True, verbose_name='Населенный пункт')
    address_street = models.CharField(max_length=200, blank=True, verbose_name='Улица')
    address_house = models.CharField(max_length=50, blank=True, verbose_name='Дом')
    address_kv = models.CharField(max_length=10, blank=True, verbose_name='Квартира')
    equip = models.CharField(max_length=200, blank=True, verbose_name='Оборудование')
    sum = models.IntegerField(blank=True, verbose_name='Сумма')
    discount = models.IntegerField(blank=True, verbose_name='Скидка')
    amount = models.IntegerField(blank=True, verbose_name='Итого')
    comment = models.CharField(max_length=500, blank=True, verbose_name='Примечание')
    id_old = models.IntegerField(verbose_name='Old Id')
    # Действует / Расторгнут
    active = models.BooleanField(verbose_name='Действующий')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Договор'
        verbose_name_plural = 'Договора'


class Payment(models.Model):
    dogovor_id = models.ForeignKey(Dogovor, on_delete=models.CASCADE)
    pay_type = models.BooleanField(verbose_name='Наличные')
    date = models.DateField(blank=False, verbose_name='Дата оплаты')
    amount = models.IntegerField(blank=False, verbose_name='Сумма')
    pay_place = models.CharField(max_length=10, blank=True, verbose_name='Место оплаты')

    class Meta:
        verbose_name = 'Оплата'
        verbose_name_plural = 'Оплаты'
