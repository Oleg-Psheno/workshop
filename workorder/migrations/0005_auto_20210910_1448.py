# Generated by Django 3.2.4 on 2021-09-10 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workorder', '0004_partitem'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='partitem',
            options={'verbose_name': 'запчасть к заказ-наряду', 'verbose_name_plural': 'запчасти к заказ-наряду'},
        ),
        migrations.AlterModelOptions(
            name='workitem',
            options={'verbose_name': 'работа к заказ-наряду', 'verbose_name_plural': 'работы к заказ-наряду'},
        ),
        migrations.AlterModelOptions(
            name='workorder',
            options={'verbose_name': 'заказ-наряд', 'verbose_name_plural': 'заказ-наряды'},
        ),
    ]
