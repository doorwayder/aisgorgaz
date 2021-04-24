from django.db import models
from django.conf import settings
from datetime import datetime, timedelta
from .param import *


class Dogovor(models.Model):
    name = models.CharField(max_length=200, blank=True, verbose_name='ФИО')
    number = models.CharField(max_length=15, blank=True, verbose_name='Номер договора')
    date = models.DateField(blank=True, verbose_name='Дата заключения договора')
    end_date = models.DateField(blank=True, null=True, verbose_name='Дата окончания договора')
    tel1 = models.CharField(max_length=10, blank=True, verbose_name='Телефон 1')
    tel2 = models.CharField(max_length=10, blank=True, verbose_name='Телефон 2')
    tel3 = models.CharField(max_length=100, blank=True, verbose_name='Телефон 3')
    fiz = models.BooleanField(verbose_name='Физлицо')
    address_city = models.CharField(max_length=100, blank=True, verbose_name='Населенный пункт')
    address_street = models.CharField(max_length=200, blank=True, verbose_name='Улица')
    address_house = models.CharField(max_length=50, blank=True, verbose_name='Дом')
    address_kv = models.CharField(max_length=10, blank=True, verbose_name='Квартира')
    equip = models.CharField(max_length=200, blank=True, verbose_name='Оборудование')
    sum = models.IntegerField(blank=True, verbose_name='Сумма')
    discount = models.IntegerField(blank=True, verbose_name='Скидка', default=0)
    amount = models.IntegerField(blank=True, verbose_name='Итого')
    comment = models.CharField(max_length=500, blank=True, verbose_name='Примечание')
    id_old = models.IntegerField(null=True, verbose_name='Old Id')
    active = models.BooleanField(default=True, verbose_name='Действующий')   # Действует / Расторгнут
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    create_time = models.DateTimeField(auto_now=True, null=True, verbose_name='Время обновления договора')

    def __str__(self):
        return self.name

    def is_expiring(self):
        if self.end_date is None:
            return False
        else:
            end = datetime.now().date() + timedelta(days=EXPIRED_DAYS)

            if self.end_date <= end and self.end_date >= datetime.today().date():
                return True
            else:
                return False

    def is_expired(self):
        if self.end_date is None:
            return False
        else:
            if self.end_date < datetime.now().date():
                return True
            else:
                return False

    def get_full_address(self):
        address = self.address_city + ', ' + self.address_street
        if self.address_house:
            address += ', ' + self.address_house
        if self.address_kv:
            address += ', ' + self.address_kv
        return address


    def get_full_phone(self):
        phone = ''
        if self.tel1:
            phone = self.tel1
            if self.tel2:
                phone += ', ' + self.tel2
            if self.tel3:
                phone += ', ' + self.tel3
        elif self.tel2:
            phone = self.tel2
            if self.tel3:
                phone += ', ' + self.tel3
        elif self.tel3:
            phone = self.tel3
        return phone

    class Meta:
        verbose_name = 'Договор'
        verbose_name_plural = 'Договора'


class Payment(models.Model):
    dogovor_id = models.ForeignKey(Dogovor, on_delete=models.CASCADE)
    pay_type = models.BooleanField(verbose_name='Наличные')
    date = models.DateField(blank=False, verbose_name='Дата оплаты')
    amount = models.IntegerField(blank=False, verbose_name='Сумма')
    pay_place = models.CharField(max_length=50, blank=True, verbose_name='Место оплаты', default='В офисе')
    comment = models.CharField(max_length=500, blank=True, verbose_name='Примечание', null=True)

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    create_time = models.DateTimeField(auto_now=True, null=True, verbose_name='Время обновления платежа')

    class Meta:
        verbose_name = 'Оплата'
        verbose_name_plural = 'Оплаты'


class Notification(models.Model):
    TYPE_CHOICES = [('SMS', 'SMS'), ('Viber', 'Viber'), ('Telegram', 'Telegram'), ('Call', 'Call')]
    dogovor_id = models.ForeignKey(Dogovor, on_delete=models.CASCADE)
    notify_type = models.CharField(max_length=10, blank=False, verbose_name='Тип уведомления', choices=TYPE_CHOICES,
                                   default='SMS')
    create_time = models.DateTimeField(auto_now_add=True, null=False, blank=False, verbose_name='Время создания уведомления')
    send_time_1 = models.DateTimeField(null=True, blank=True, verbose_name='Время отправки уведомления')
    send_time_2 = models.DateTimeField(null=True, blank=True, verbose_name='Время отправки уведомления')
    success_1 = models.BooleanField(default=False, verbose_name='Успешно')
    success_2 = models.BooleanField(default=False, verbose_name='Успешно')
    comment = models.CharField(max_length=500, blank=True, verbose_name='Примечание', null=True)

    def __str__(self):
        return self.dogovor_id.name

    class Meta:
        verbose_name = 'Уведомление'
        verbose_name_plural = 'Уведомления'


class Worker(models.Model):
    name = models.CharField(max_length=100, blank=True, verbose_name='ФИО')
    func = models.CharField(max_length=100, blank=True, verbose_name='Должность')
    description = models.CharField(max_length=500, blank=True, null=True, verbose_name='Описание')
    active = models.BooleanField(default=True, verbose_name='Работает')   # Работает / Уволился

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'


class Order(models.Model):
    name = models.CharField(max_length=200, verbose_name='ФИО')
    address = models.CharField(max_length=300, verbose_name='Адрес')
    tel = models.CharField(max_length=100, blank=True, null=True, default='', verbose_name='Телефон')
    job = models.CharField(max_length=200, verbose_name='Работы')
    date = models.DateField(verbose_name='Дата')
    #  привязка к договору (необязательна)
    dogovor_id = models.ForeignKey(Dogovor, blank=True, null=True, on_delete=models.CASCADE)
    amount = models.IntegerField(blank=True,  null=True, verbose_name='Итого')
    comment = models.CharField(max_length=500, blank=True, null=True, verbose_name='Примечание')
    worker = models.ForeignKey(Worker, blank=True, null=True, on_delete=models.PROTECT)
    completed = models.BooleanField(verbose_name='Выполнен')

    def __str__(self):
        return str(self.pk) + ' - ' + self.name

    class Meta:
        verbose_name = 'Наряд'
        verbose_name_plural = 'Наряды'
