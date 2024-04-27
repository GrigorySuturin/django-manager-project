from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from .models import ManagerItem


class ManagerListView(ListView):
    template_name = 'manager_app/index.html'
    model = ManagerItem
    context_object_name = 'manager_items'


class ManagerDetailView(DetailView):
    model = ManagerItem
