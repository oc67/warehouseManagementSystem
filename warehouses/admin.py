from django.contrib import admin
from .models import Warehouse

# Register your models here.

class WarehouseAdmin(admin.ModelAdmin):

    list_display=[
     "name",
     "manager_full_name",
     "country",
     "municipality",
     "address_line",
     "organisation",
     "is_active",
     "is_location_for_receipts",
     "is_location_for_shipments",

     ]


admin.site.register(Warehouse,WarehouseAdmin)

