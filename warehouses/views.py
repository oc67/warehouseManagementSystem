from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DetailView
from .models import Warehouse

# Create your views here.

class WarehouseListView(ListView):
    model=Warehouse
    template_name="warehouse/warehouse_list.html"


class WarehouseCreationView(CreateView):
    model=Warehouse
    template_name="warehouse/warehouse_create.html"

class WarehouseDetailView(DetailView):
    model=Warehouse
    template_name="warehouse/warehouse_detail.html"