# Generated by Django 3.1.6 on 2021-04-24 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dogovor', '0012_auto_20210424_2151'),
    ]

    operations = [
        migrations.AddField(
            model_name='worker',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Работает'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='create_time',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Время обновления платежа'),
        ),
    ]