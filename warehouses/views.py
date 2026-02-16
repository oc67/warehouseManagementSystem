from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView
from .models import Warehouse

# Create your views here.

class WarehouseListView(ListView):
    model=Warehouse
    template_name="warehouse/warehouse_list.html"



   


class WarehouseCreationView(CreateView):
    model=Warehouse
    template_name="warehouse/warehouse_create.html"
    fields=["name","manager_full_name","country","municipality",
            "address_line","organisation","is_active","is_location_for_receipts",
            "is_location_for_shipments"]

class WarehouseDetailView(UpdateView):
    model=Warehouse
    fields="__all__"
    template_name="warehouse/warehouse_detail.html"
    context_object_name="warehouse"