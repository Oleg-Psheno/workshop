# Generated by Django 3.2.4 on 2021-09-10 12:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('regular_price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='WorkOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('status', models.CharField(choices=[('CR', 'создан'), ('RD', 'обработан'), ('DN', 'выполнен')], default='CR', max_length=2)),
                ('pay_status', models.CharField(choices=[('PD', 'оплачено'), ('NP', 'не оплачено'), ('PP', 'предоплата')], default='NP', max_length=2)),
                ('client', models.ForeignKey(max_length=128, on_delete=django.db.models.deletion.CASCADE, related_name='clientorder', to=settings.AUTH_USER_MODEL)),
                ('creator', models.ForeignKey(max_length=128, on_delete=django.db.models.deletion.CASCADE, related_name='ordercreator', to=settings.AUTH_USER_MODEL)),
                ('employee', models.ForeignKey(max_length=128, on_delete=django.db.models.deletion.CASCADE, related_name='employeeorder', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WorkItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workorder.job')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='workorder.workorder')),
            ],
        ),
    ]
