# Generated by Django 2.2.6 on 2021-04-12 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0003_auto_20210412_2302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='type',
            field=models.CharField(choices=[('-', 'Списание'), ('+', 'Пополнение')], max_length=10, verbose_name='Тип транзакции'),
        ),
    ]