from django.db import models
from django.contrib.auth.models import AbstractUser

# class User(AbstractUser):
#     pass

class Order(models.Model):
    FORMING = 'FM'
    READY = 'RD'
    DONE = 'DN'
    ORDER_STATUS_CHOISES = ((FORMING,'формируется'),(READY,'обработан'),(DONE,'выполнен'),)

    user = models.CharField(max_length=20)
    phone = models.CharField(max_length=12, blank=True, null=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    status = models.CharField(max_length=2, choices=ORDER_STATUS_CHOISES,default=FORMING)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.user}'




