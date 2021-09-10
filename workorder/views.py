from django.shortcuts import render
from django.views.generic import TemplateView


class OrderView(TemplateView):
    template_name = 'order.html'
