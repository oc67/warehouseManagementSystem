from django.urls import path
from .views import WarehouseListView, WarehouseCreationView, WarehouseListView, WarehouseDetailView

urlpatterns=[
    path("",WarehouseListView.as_view(),name="warehouse_list"),
    path("new/",WarehouseCreationView.as_view(),name="warehouse_create"),
    path("list/",WarehouseListView.as_view(),name="warehouse_list"),
    path("warehouse/<int:pk>/",WarehouseDetailView.as_view(),name="warehouse_detail"),

]