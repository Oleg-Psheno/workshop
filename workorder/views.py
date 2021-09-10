from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import WorkOrder, Job, WorkItem

class OrderView(ListView):
    model = WorkOrder
    template_name = 'order.html'
    context_object_name = 'orders'


class OrderDetailView(DetailView):
    model = WorkOrder
    template_name = 'detail.html'
    context_object_name = 'order'
    
    def get_context_data(self, **kwargs):
        context = super(OrderDetailView, self).get_context_data(**kwargs)
        context['jobs'] = WorkItem.objects.filter(order_id=context['object'].id)

        print(context)
        return context



