from django.db import models
from django.contrib.auth.models import User

class Dogovor(models.Model):
    name = models.CharField(max_length=200, verbose_name='Имя')
    comment = models.CharField(max_length=500, blank=True, verbose_name='Примечание')
    number = models.IntegerField(verbose_name='Номер договора')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Договор'
        verbose_name_plural = 'Договора'

