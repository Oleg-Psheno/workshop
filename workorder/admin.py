from django.contrib import admin
from .models import Job,WorkOrder, WorkItem

admin.site.register(Job)
admin.site.register(WorkItem)
admin.site.register(WorkOrder)