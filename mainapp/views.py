from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from mainapp.forms import MainForm
from mainapp.models import Order
from django.urls import reverse_lazy

class IndexView(FormView):
    model = Order
    template_name = 'index.html'
    form_class = MainForm
    success_url = '/'
    # success_url = reverse_lazy('index')

    def form_valid(self, form):
        super(IndexView, self).form_valid(form)
        print('form valid')
        form.save()
        return super(IndexView, self).form_valid(form)

    def form_invalid(self, form):
        super(IndexView, self).form_invalid(form)
        print('form invalid')
        return super(IndexView, self).form_invalid(form)

    # def get_context_data(self, **kwargs):
    #     context = super(IndexView, self).get_context_data(**kwargs)
    #     if self.request.method == 'POST':
    #         print('lalal')
    #     else:
    #         print('asasa')
    #     context['title'] = 'Новый заказ'
    #     context['form'] = self.form_class
    #     return context
    #
    #
    #
    # def form_valid(self,form):
    #     self.get_context_data()
    #     form.save()
    #     return super(IndexView, self).form_valid(form)
