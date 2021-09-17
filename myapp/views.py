from django.shortcuts import render
from . models import *
from django.views.generic import ListView, DetailView
from django.http import Http404

# Create your views here.

class NumberListView(ListView):
    model = Number
    template_name = 'myapp/main.html'
    ordering = ['id']
    paginate_by = 5
    paginate_orphans = 1

    def get_context_data(self, *args, **kwargs):
        try:
            return super(NumberListView, self).get_context_data(*args, **kwargs)
        except Http404:
            self.kwargs['page'] = 1
            return super(NumberListView, self).get_context_data(*args, **kwargs)

class NumberDetailView(DetailView):
    model = Number
    template_name = 'myapp/index.html'