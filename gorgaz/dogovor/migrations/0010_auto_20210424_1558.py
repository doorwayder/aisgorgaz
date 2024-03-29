# Generated by Django 3.1.6 on 2021-04-24 15:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dogovor', '0009_auto_20210424_1526'),
    ]

    operations = [
        migrations.AddField(
            model_name='dogovor',
            name='create_time',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Время создания договора'),
        ),
        migrations.AddField(
            model_name='dogovor',
            name='update_time',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Время обновления договора'),
        ),
        migrations.AlterField(
            model_name='dogovor',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
