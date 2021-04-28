# Generated by Django 3.2 on 2021-04-28 13:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dogovor', '0014_auto_20210426_1834'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dogovor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dogovor.dogovor')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'План',
                'verbose_name_plural': 'Планы',
                'unique_together': {('dogovor_id', 'user_id')},
            },
        ),
    ]