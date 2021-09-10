from django.contrib import admin
from .models import Job,WorkOrder, WorkItem, PartItem

admin.site.register(Job)
admin.site.register(WorkItem)
admin.site.register(WorkOrder)
admin.site.register(PartItem)