from django.db import models
from authapp.models import User

class WorkOrder(models.Model):
    CREATED = 'CR'
    READY = 'RD'
    DONE = 'DN'
    ORDER_STATUS_CHOISES = ((CREATED, 'создан'), (READY, 'обработан'), (DONE, 'выполнен'),)
    PAID = 'PD'
    NOT_PAID = 'NP'
    PRE_PAID = 'PP'
    PAY_STATUS_CHOISES = ((PAID,'оплачено'), (NOT_PAID,'не оплачено'),(PRE_PAID,'предоплата'))

    creator = models.ForeignKey(to=User,max_length=128,on_delete=models.CASCADE, related_name='ordercreator') #ключ к другой модели?
    employee = models.ForeignKey(to=User,max_length=128,on_delete=models.CASCADE, related_name='employeeorder') #ключ к другой модели?
    client = models.ForeignKey(to=User,max_length=128,on_delete=models.CASCADE, related_name='clientorder')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    status =  models.CharField(max_length=2, choices=ORDER_STATUS_CHOISES, default=CREATED)
    pay_status = models.CharField(max_length=2, choices=PAY_STATUS_CHOISES, default=NOT_PAID)

    def __str__(self):
        return f'Заказ №{self.id} клиента {self.client} от {self.created_at}'

class Job(models.Model):
    name = models.CharField(max_length=128)
    regular_price = models.IntegerField()
    # unit = models.CharField(max_length=10) надо ли?
    def __str__(self):
        return f'{self.name}'


class WorkItem(models.Model):
    order = models.ForeignKey(WorkOrder, on_delete=models.CASCADE, related_name='order')
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    quantity = models.IntegerField(verbose_name='количество', default=1)
    def __str__(self):
        return f'К заказу {self.order_id}'
# class WorkPartItme(models.Model):
#     order = models.ForeignKey(WorkOrder, on_delete=models.CASCADE)


