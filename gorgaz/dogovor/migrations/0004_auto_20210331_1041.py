# Generated by Django 3.1.7 on 2021-03-31 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dogovor', '0003_auto_20210219_0857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dogovor',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Действующий'),
        ),
        migrations.AlterField(
            model_name='dogovor',
            name='id_old',
            field=models.IntegerField(null=True, verbose_name='Old Id'),
        ),
        migrations.AlterField(
            model_name='dogovor',
            name='tel1',
            field=models.CharField(blank=True, max_length=10, verbose_name='Телефон 1'),
        ),
        migrations.AlterField(
            model_name='dogovor',
            name='tel2',
            field=models.CharField(blank=True, max_length=10, verbose_name='Телефон 2'),
        ),
        migrations.AlterField(
            model_name='dogovor',
            name='tel3',
            field=models.CharField(blank=True, max_length=100, verbose_name='Телефон 3'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='pay_place',
            field=models.CharField(blank=True, choices=[('в офисе', 'в офисе'), ('обходчику', 'обходчику'), ('квитанция', 'квитанция')], default='В офисе', max_length=10, verbose_name='Место оплаты'),
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tel', models.CharField(blank=True, max_length=10, verbose_name='Телефон')),
                ('notify_type', models.CharField(choices=[('SMS', 'SMS'), ('Viber', 'Viber'), ('Telegram', 'Telegram')], default='SMS', max_length=10, verbose_name='Тип уведомления')),
                ('time', models.DateTimeField(null=True, verbose_name='Даза отправки уведомления')),
                ('success', models.BooleanField(default=False, verbose_name='Успешно')),
                ('dogovor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dogovor.dogovor')),
            ],
        ),
    ]
